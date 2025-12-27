from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from checkout.models import Order, OrderItem
from catalog.models import Product, DigitalVariant, Wishlist
from .models import Address

# run tests = `python manage.py test accounts`

class AccountViewsTestCase(TestCase):
    """
    Tests for account pages and auth flows.

    setUp: create a user, sample product and variant used across tests.
    Reminder: setUp runs before each test, so data is fresh for isolation.
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # Create a product + variant for order-related tests
        self.product = Product.objects.create(
            name='Test Game',
            slug='test-game',
            description='A test game',
            price=59.99,
            product_type='base_game'
        )
        self.variant = DigitalVariant.objects.create(
            product=self.product,
            platform='xbox',
            edition='standard',
            price_override=69.99
        )

    def test_order_history_requires_login(self):
        """
        Ensure the dashboard/order history redirects anonymous users.

        Reminder: use `reverse('accounts:dashboard')` to resolve the URL name.
        Result should be a 302 redirect to the login page for unauthenticated requests.
        """
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_order_history_shows_orders(self):
        """
        When logged in, user's orders should be visible on the dashboard.

        Steps:
        - log in
        - create an Order and OrderItem (snapshotted data)
        - request dashboard and assert the product name and order number appear
        """
        self.client.login(username='testuser', password='testpass123')
        # Create an order for the user
        order = Order.objects.create(
            user=self.user,
            full_name='Test User',
            email='test@example.com',
            street_address_1='123 Test St',
            city='Test City',
            postcode='12345',
            country='GB',
            total_amount=49.99,
            payment_status='paid'
        )
        # Add an order item with snapshot data
        OrderItem.objects.create(
            order=order,
            product=self.product,
            variant=self.variant,
            product_name='Test Game',
            product_sku='TEST-001',
            variant_details='Xbox Standard Edition',
            quantity=1,
            unit_price=49.99
        )

        response = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(response.status_code, 200)
        # assertContains automatically converts response content to text 
        # and searches for the substring.
        self.assertContains(response, 'Test Game')
        self.assertContains(response, order.order_number)

    def test_empty_order_history(self):
        """
        Logged-in user with no orders sees the empty-state message.

        Reminder: cover the 'no orders' template path to avoid regressions.
        """
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Orders Yet')

    def test_login_success(self):
        """
        POST valid credentials should authenticate and redirect.

        Reminder: check `response.wsgi_request.user.is_authenticated` for login state.
        """
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_invalid_credentials(self):
        """
        Invalid credentials should re-render the login form with an error.

        Note: the exact message can change if you customise auth; assert a substring.
        """
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        # Expect the standard auth non-field error text to appear in the page
        self.assertContains(response, 'Please enter a correct username and password')

    def test_signup_creates_user(self):
        """
        POSTing the signup form should create a new user and redirect.

        Reminder: use unique usernames/emails to avoid collisions (duplicates of SKUs/Keys) in tests.
        """
        response = self.client.post(reverse('accounts:signup'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'complexpass123',
            'password2': 'complexpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_logout(self):
        """
        Logout should redirect and subsequent protected pages should require login.
        """
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)

        # After logout, dashboard should redirect to login
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(response.status_code, 302)


class AddressManagementTestCase(TestCase):
    """
    Tests for address add/delete flows.

    Reminder: when posting forms, provide all required fields matching your `AddressForm`.
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_add_address(self):
        """
        Posting the add address form should redirect on success and create the Address.

        If this fails (status 200), inspect `response.context['form'].errors` to see missing fields.
        """
        response = self.client.post(reverse('accounts:add_address'), {
            'full_name': 'John Smith',
            'address_line_1': '123 Main St',
            'address_line_2': '',
            'city': 'Test City',
            'postcode': '12345',
            'country': 'GB',
            'address_type': 'billing'
        })
        # Successful form submission should redirect (302)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Address.objects.filter(user=self.user, full_name='John Smith').exists())

    def test_delete_address(self):
        """
        AJAX delete endpoint should remove the address and return success.
        """
        address = Address.objects.create(
            user=self.user,
            full_name='Test Address',
            address_line_1='123 Test St',
            city='Test City',
            postcode='12345',
            country='GB',
        )

        response = self.client.post(
            reverse('accounts:delete_address', args=[address.id]),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Address.objects.filter(id=address.id).exists())


class WishlistTestCase(TestCase):
    """
    Tests for wishlist toggle and display.

    Reminder: AJAX endpoints return JSON; use `response.json()` to inspect.
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.product = Product.objects.create(
            name='Test Game',
            slug='test-game',
            description='A test game',
            price=49.99,
            product_type='base_game'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_toggle_wishlist_add(self):
        """
        POST to toggle should add product when not already in wishlist.
        """
        response = self.client.post(
            reverse('accounts:toggle_wishlist', args=[self.product.id]),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertTrue(data['in_wishlist'])
        self.assertTrue(Wishlist.objects.filter(user=self.user, product=self.product).exists())

    def test_toggle_wishlist_remove(self):
        """
        If item exists, toggle should remove it and return in_wishlist=False.
        """
        Wishlist.objects.create(user=self.user, product=self.product)

        response = self.client.post(
            reverse('accounts:toggle_wishlist', args=[self.product.id]),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertFalse(data['in_wishlist'])
        self.assertFalse(Wishlist.objects.filter(user=self.user, product=self.product).exists())

    def test_wishlist_page_shows_items(self):
        """
        Wishlist page should render and include product names for items in the wishlist.
        """
        Wishlist.objects.create(user=self.user, product=self.product)

        response = self.client.get(reverse('accounts:wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)