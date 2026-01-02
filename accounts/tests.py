from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import DigitalVariant, Product, Wishlist
from checkout.models import Order, OrderItem

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
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        # Create a product + variant for order-related tests
        self.product = Product.objects.create(
            name="Test Game",
            slug="test-game",
            description="A test game",
            price=59.99,
            product_type="base_game",
        )
        self.variant = DigitalVariant.objects.create(
            product=self.product,
            platform="xbox",
            edition="standard",
            price_override=69.99,
        )

    def test_order_history_requires_login(self):
        """
        Ensure the dashboard/order history redirects anonymous users.

        Reminder: use `reverse('accounts:dashboard')` to resolve the URL name.
        Result should be a 302 redirect to the login page
        for unauthenticated requests.
        """
        response = self.client.get(reverse("accounts:dashboard"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_order_history_shows_orders(self):
        """
        When logged in, user's orders should be visible on the dashboard.

        Steps:
        - log in
        - create an Order and OrderItem (snapshotted data)
        - request dashboard and assert the product name and order number appear
        """
        self.client.login(username="testuser", password="testpass123")
        # Create an order for the user
        order = Order.objects.create(
            user=self.user,
            full_name="Test User",
            email="test@example.com",
            street_address_1="123 Test St",
            city="Test City",
            postcode="12345",
            country="GB",
            total_amount=49.99,
            payment_status="paid",
        )
        # Add an order item with snapshot data
        OrderItem.objects.create(
            order=order,
            product=self.product,
            variant=self.variant,
            product_name="Test Game",
            product_sku="TEST-001",
            variant_details="Xbox Standard Edition",
            quantity=1,
            unit_price=49.99,
        )

        response = self.client.get(reverse("accounts:dashboard"))
        self.assertEqual(response.status_code, 200)
        # assertContains automatically converts response content to text
        # and searches for the substring.
        self.assertContains(response, "Test Game")
        self.assertContains(response, order.order_number)

    def test_empty_order_history(self):
        """
        Logged-in user with no orders sees the empty-state message.

        Reminder: cover the 'no orders' template path to avoid regressions.
        """
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("accounts:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Orders Yet")

    def test_login_success(self):
        """
        POST valid credentials should authenticate and redirect.

        Reminder: check `response.wsgi_request.user.is_authenticated`
        for login state.
        """
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "testuser", "password": "testpass123"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_invalid_credentials(self):
        """
        Invalid credentials should re-render the login form with an error.

        Note: the exact message can change if you
        customise auth; assert a substring.
        """
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "testuser", "password": "wrongpassword"},
        )
        self.assertEqual(response.status_code, 200)
        # Expect the standard auth non-field error text to appear in the page
        self.assertContains(
            response, "Please enter a correct username and password"
        )

    def test_signup_creates_user(self):
        """
        POSTing the signup form should create a new user and redirect.

        Reminder: use unique usernames/emails to avoid
        collisions (duplicates of SKUs/Keys) in tests.
        """
        response = self.client.post(
            reverse("accounts:signup"),
            {
                "username": "newuser",
                "email": "new@example.com",
                "password1": "complexpass123",
                "password2": "complexpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_logout(self):
        """
        Logout should redirect and subsequent protected pages
        should require login.
        """
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("accounts:logout"))
        self.assertEqual(response.status_code, 302)

        # After logout, dashboard should redirect to login
        response = self.client.get(reverse("accounts:dashboard"))
        self.assertEqual(response.status_code, 302)


class AddressManagementTestCase(TestCase):
    """
    Tests for address add/delete flows.

    Reminder: when posting forms, provide all required
    fields matching your `AddressForm`.
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.client.login(username="testuser", password="testpass123")

    def test_add_address(self):
        """
        Posting the add address form should redirect on success
        and create the Address.

        If this fails (status 200), inspect
        `response.context['form'].errors` to see missing fields.
        """
        response = self.client.post(
            reverse("accounts:add_address"),
            {
                "full_name": "John Smith",
                "address_line_1": "123 Main St",
                "address_line_2": "",
                "city": "Test City",
                "postcode": "12345",
                "country": "GB",
                "address_type": "billing",
            },
        )
        # Successful form submission should redirect (302)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Address.objects.filter(
                user=self.user, full_name="John Smith"
            ).exists()
        )

    def test_delete_address(self):
        """
        AJAX delete endpoint should remove the address and return success.
        """
        address = Address.objects.create(
            user=self.user,
            full_name="Test Address",
            address_line_1="123 Test St",
            city="Test City",
            postcode="12345",
            country="GB",
        )

        response = self.client.post(
            reverse("accounts:delete_address", args=[address.id]),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
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
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.product = Product.objects.create(
            name="Test Game",
            slug="test-game",
            description="A test game",
            price=49.99,
            product_type="base_game",
        )
        self.client.login(username="testuser", password="testpass123")

    def test_toggle_wishlist_add(self):
        """
        POST to toggle should add product when not already in wishlist.
        """
        response = self.client.post(
            reverse("accounts:toggle_wishlist", args=[self.product.id]),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertTrue(data["in_wishlist"])
        self.assertTrue(
            Wishlist.objects.filter(
                user=self.user, product=self.product
            ).exists()
        )

    def test_toggle_wishlist_remove(self):
        """
        If item exists, toggle should remove it and return in_wishlist=False.
        """
        Wishlist.objects.create(user=self.user, product=self.product)

        response = self.client.post(
            reverse("accounts:toggle_wishlist", args=[self.product.id]),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertFalse(data["in_wishlist"])
        self.assertFalse(
            Wishlist.objects.filter(
                user=self.user, product=self.product
            ).exists()
        )

    def test_wishlist_page_shows_items(self):
        """
        Wishlist page should render and include product names
        for items in the wishlist.
        """
        Wishlist.objects.create(user=self.user, product=self.product)

        response = self.client.get(reverse("accounts:wishlist"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)


class OrderDetailTestCase(TestCase):
    """Tests for order detail view access control"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.product = Product.objects.create(
            name="Test Game",
            slug="test-game",
            description="A test game",
            price=59.99,
            product_type="base_game",
        )
        self.variant = DigitalVariant.objects.create(
            product=self.product, platform="pc", edition="standard"
        )
        self.client.login(username="testuser", password="testpass123")

    def test_order_detail_wrong_user(self):
        """Test order detail view returns 404 for wrong user"""
        from checkout.models import Order

        other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="testpass123",
        )

        order = Order.objects.create(
            user=other_user,  # Different user
            full_name="Other User",
            email="other@example.com",
            street_address_1="456 Other St",
            city="Other City",
            postcode="54321",
            country="GB",
            total_amount=29.99,
            payment_status="paid",
        )

        response = self.client.get(
            reverse("accounts:order_detail", args=[order.order_number])
        )

        self.assertEqual(response.status_code, 404)

    def test_order_detail_nonexistent_order(self):
        """Test order detail view returns 404 for non-existent order"""
        response = self.client.get(
            reverse("accounts:order_detail", args=["FAKE-ORDER-NUMBER"])
        )

        self.assertEqual(response.status_code, 404)

    def test_order_detail_view(self):
        """Order detail returns 200 for owner
        (render is faked with a real HttpResponse).
        """
        from unittest.mock import patch

        from django.http import HttpResponse

        from checkout.models import Order, OrderItem

        order = Order.objects.create(
            user=self.user,
            full_name="Test User",
            email="test@example.com",
            street_address_1="123 Test St",
            city="Test City",
            postcode="12345",
            country="GB",
            total_amount=59.99,
            payment_status="paid",
        )

        OrderItem.objects.create(
            order=order,
            product=self.product,
            variant=self.variant,
            product_name="Test Game",
            product_sku="TEST-001",
            variant_details="PC Standard Edition",
            quantity=1,
            unit_price=59.99,
        )

        def _fake_render(
            request, template_name, context=None, *args, **kwargs
        ):
            return HttpResponse("ok")

        with patch("accounts.views.render", new=_fake_render):
            resp = self.client.get(
                reverse("accounts:order_detail", args=[order.order_number])
            )
            self.assertEqual(resp.status_code, 200)


def test_order_detail_view_loads(self):
    """Order detail returns 404 for non-owner or non-existent order."""
    from checkout.models import Order

    other_user = User.objects.create_user(
        username="otheruser", email="other@example.com", password="testpass123"
    )
    order = Order.objects.create(
        user=other_user,
        full_name="Other User",
        email="other@example.com",
        street_address_1="456 Other St",
        city="Other City",
        postcode="54321",
        country="GB",
        total_amount=29.99,
        payment_status="paid",
    )

    resp = self.client.get(
        reverse("accounts:order_detail", args=[order.order_number])
    )
    self.assertEqual(resp.status_code, 404)

    resp = self.client.get(
        reverse("accounts:order_detail", args=["FAKE-ORDER-NUMBER"])
    )
    self.assertEqual(resp.status_code, 404)


class AddressEditTestCase(TestCase):
    """Tests for address editing functionality"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.address = Address.objects.create(
            user=self.user,
            full_name="John Doe",
            address_line_1="123 Old St",
            city="Old City",
            postcode="12345",
            country="GB",
            address_type="billing",
        )
        self.client.login(username="testuser", password="testpass123")

    def test_edit_address_get(self):
        """Test edit address form displays current data"""
        response = self.client.get(
            reverse("accounts:edit_address", args=[self.address.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertContains(response, "123 Old St")
        self.assertEqual(response.context["address"], self.address)

    def test_edit_address_post(self):
        """Test edit address form saves changes"""
        response = self.client.post(
            reverse("accounts:edit_address", args=[self.address.id]),
            {
                "full_name": "Jane Doe",
                "address_line_1": "456 New St",
                "address_line_2": "",
                "city": "New City",
                "postcode": "54321",
                "country": "GB",
                "address_type": "shipping",
            },
        )

        self.assertEqual(response.status_code, 302)

        # Refresh from database
        self.address.refresh_from_db()
        self.assertEqual(self.address.full_name, "Jane Doe")
        self.assertEqual(self.address.address_line_1, "456 New St")
        self.assertEqual(self.address.address_type, "shipping")

    def test_edit_address_wrong_user(self):
        """Test editing address of another user returns 404"""
        other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="testpass123",
        )

        other_address = Address.objects.create(
            user=other_user,
            full_name="Other User",
            address_line_1="999 Other St",
            city="Other City",
            postcode="99999",
            country="GB",
        )

        response = self.client.get(
            reverse("accounts:edit_address", args=[other_address.id])
        )

        self.assertEqual(response.status_code, 404)


class AuthenticationEdgeCaseTests(TestCase):
    """Tests for authentication edge cases and redirects"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

    def test_login_already_authenticated(self):
        """Test login redirect when user already logged in"""
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("accounts:login"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")  # Should redirect to home

    def test_login_with_next_parameter(self):
        """Test login redirects to next parameter after successful login"""
        response = self.client.post(
            reverse("accounts:login") + "?next=/cart/",
            {"username": "testuser", "password": "testpass123"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/cart/")

    def test_signup_already_authenticated(self):
        """Test signup redirect when user already logged in"""
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("accounts:signup"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

    def test_signup_with_next_parameter(self):
        """
        Test signup redirects to next parameter after successful registration
        """
        response = self.client.post(
            reverse("accounts:signup") + "?next=/checkout/",
            {
                "username": "newuser",
                "email": "new@example.com",
                "password1": "complexpass123",
                "password2": "complexpass123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/checkout/")

    def test_logout_unauthenticated(self):
        """Test logout when user not authenticated"""
        response = self.client.get(reverse("accounts:logout"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")


class WishlistVariantTestCase(TestCase):
    """Tests for wishlist with product variants"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.product = Product.objects.create(
            name="Test Game",
            slug="test-game",
            description="A test game",
            price=49.99,
            product_type="base_game",
        )
        self.variant = DigitalVariant.objects.create(
            product=self.product,
            platform="pc",
            edition="ultimate",
            price_override=79.99,
        )
        self.client.login(username="testuser", password="testpass123")

    def test_toggle_wishlist_with_variant(self):
        """Test adding product variant to wishlist"""
        response = self.client.post(
            reverse("accounts:toggle_wishlist", args=[self.product.id]),
            {"variant_id": self.variant.id},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertTrue(data["in_wishlist"])

        # Check variant is in wishlist
        wishlist_item = Wishlist.objects.get(
            user=self.user, product=self.product
        )
        self.assertEqual(wishlist_item.variant, self.variant)

    def test_toggle_wishlist_invalid_variant(self):
        """Test toggle wishlist with invalid variant ID"""
        response = self.client.post(
            reverse("accounts:toggle_wishlist", args=[self.product.id]),
            {"variant_id": 99999},  # Non-existent variant
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("Invalid variant", data["message"])

    def test_check_wishlist_status(self):
        """Test checking if product/variant is in wishlist"""
        # Add to wishlist first
        Wishlist.objects.create(
            user=self.user, product=self.product, variant=self.variant
        )

        response = self.client.get(
            reverse("accounts:check_wishlist", args=[self.product.id]),
            {"variant_id": self.variant.id},
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertTrue(data["in_wishlist"])

    def test_check_wishlist_not_in_list(self):
        """Test checking wishlist status when item not in wishlist"""
        response = self.client.get(
            reverse("accounts:check_wishlist", args=[self.product.id])
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertFalse(data["in_wishlist"])


class SavedAddressesTestCase(TestCase):
    """Tests for saved addresses listing"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.client.login(username="testuser", password="testpass123")

    def test_saved_addresses_empty(self):
        """Test saved addresses page with no addresses"""
        response = self.client.get(reverse("accounts:saved_addresses"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["address_count"], 0)
        self.assertEqual(len(response.context["addresses"]), 0)

    def test_saved_addresses_with_data(self):
        """Test saved addresses page with addresses"""
        Address.objects.create(
            user=self.user,
            full_name="Home Address",
            address_line_1="123 Home St",
            city="Home City",
            postcode="12345",
            country="GB",
            address_type="billing",
        )

        Address.objects.create(
            user=self.user,
            full_name="Work Address",
            address_line_1="456 Work Ave",
            city="Work City",
            postcode="54321",
            country="GB",
            address_type="shipping",
        )

        response = self.client.get(reverse("accounts:saved_addresses"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["address_count"], 2)
        self.assertContains(response, "Home Address")
        self.assertContains(response, "Work Address")


class DeleteAddressErrorTestCase(TestCase):
    """Tests for address deletion error handling"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.client.login(username="testuser", password="testpass123")

    def test_delete_nonexistent_address(self):
        """Test deleting non-existent address returns 404"""
        response = self.client.post(
            reverse("accounts:delete_address", args=[99999]),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 404)
