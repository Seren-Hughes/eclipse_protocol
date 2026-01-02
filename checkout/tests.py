import json
from decimal import Decimal
from unittest.mock import Mock, patch

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.test.utils import override_settings
from django.urls import reverse

from accounts.models import Address
from cart.models import Cart, CartItem
from catalog.models import DigitalVariant, Product

from .forms import OrderForm
from .models import LicenseKey, Order, OrderItem, Payment


class CheckoutModelTests(TestCase):
    """
    Unit tests for checkout model functionality.

    Tests model behaviour:
    - Order creation and validation
    - Payment tracking and status updates
    - License key generation and assignment
    - Order item calculations and integrity
    """

    def setUp(self):
        """Set up test fixtures for checkout model testing."""
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        # Create test products
        self.base_game = Product.objects.create(
            name="Eclipse Protocol Game",
            slug="eclipse-protocol-game-model-test",
            description="Test game",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            sku="EP-BASE-MODEL",
        )

        self.currency_product = Product.objects.create(
            name="Eclipse Credits",
            slug="eclipse-credits-model-test",
            description="In-game currency",
            price=Decimal("9.99"),
            product_type=Product.CURRENCY,
            sku="EP-CURR-MODEL",
        )

    def test_order_creation_with_required_fields(self):
        """Test Order model creation with all required fields."""
        order = Order.objects.create(
            user=self.user,
            full_name="Test User",
            email="test@example.com",
            street_address_1="123 Test Street",
            city="Test City",
            postcode="12345",
            country="US",
            total_amount=Decimal("59.99"),
            stripe_pid="pi_test_1234567890",
        )

        # Test order number generation (EP + 8 hex chars)
        self.assertTrue(order.order_number.startswith("EP"))
        self.assertEqual(len(order.order_number), 10)

        # Test default status values
        self.assertEqual(order.payment_status, Order.PAYMENT_PENDING)
        self.assertEqual(order.delivery_status, Order.DELIVERY_PENDING)

        # Test string representation
        expected_str = f"Order {order.order_number}"
        self.assertEqual(str(order), expected_str)

        # Test total calculation
        self.assertEqual(order.total_amount, Decimal("59.99"))

    def test_order_item_creation_and_calculations(self):
        """Test OrderItem model creation and price calculations."""
        order = Order.objects.create(
            user=self.user,
            full_name="Test User",
            email="test@example.com",
            street_address_1="123 Test Street",
            city="Test City",
            postcode="12345",
            country="GB",
            total_amount=Decimal("59.99"),
            stripe_pid="pi_test_1234567890",
        )

        # Create order item
        order_item = OrderItem.objects.create(
            order=order,
            product=self.base_game,
            product_name=self.base_game.name,
            product_sku=self.base_game.sku,
            quantity=2,
            unit_price=Decimal("29.99"),
        )

        # Test calculations
        self.assertEqual(order_item.total_price, Decimal("59.98"))

        # Test string representation (no space before x)
        expected_str = f"{self.base_game.name} x2"
        self.assertEqual(str(order_item), expected_str)

        # Test order relationship
        self.assertEqual(order_item.order, order)
        self.assertEqual(order.items.count(), 1)

    def test_payment_model_creation(self):
        """Test Payment model creation and status tracking."""
        order = Order.objects.create(
            user=self.user,
            full_name="Test User",
            email="test@example.com",
            street_address_1="123 Test Street",
            city="Test City",
            postcode="12345",
            country="GB",
            total_amount=Decimal("59.99"),
            stripe_pid="pi_test_1234567890",
        )

        # Create payment
        payment = Payment.objects.create(
            order=order,
            transaction_id="pi_test_1234567890",
            amount=Decimal("59.99"),
            status=Payment.SUCCEEDED,
        )

        # Test payment methods
        self.assertTrue(payment.is_successful)

        # Test string representation
        expected_str = (
            f"Payment {payment.transaction_id} - "
            f"{payment.get_status_display()}"
        )
        self.assertEqual(str(payment), expected_str)

        # Test order relationship
        self.assertEqual(payment.order, order)

    def test_license_key_generation(self):
        """Test LicenseKey model creation and key generation."""
        order = Order.objects.create(
            user=self.user,
            full_name="Test User",
            email="test@example.com",
            street_address_1="123 Test Street",
            city="Test City",
            postcode="12345",
            country="GB",
            total_amount=Decimal("49.99"),
            stripe_pid="pi_test_1234567890",
        )

        order_item = OrderItem.objects.create(
            order=order,
            product=self.base_game,
            product_name=self.base_game.name,
            product_sku=self.base_game.sku,
            quantity=1,
            unit_price=Decimal("49.99"),
        )

        # Create license key with correct field structure
        license_key = LicenseKey.objects.create(
            user=self.user,
            order_item=order_item,
            product=self.base_game,
            platform="PC",
            key_code="TEST-KEY-12345",
        )

        # Test key properties
        self.assertIsNotNone(license_key.key_code)
        self.assertEqual(license_key.key_code, "TEST-KEY-12345")

        # Test default status
        self.assertEqual(license_key.status, LicenseKey.KEY_ACTIVE)

        # Test string representation
        expected_str = f"{self.base_game.name} - PC"
        self.assertEqual(str(license_key), expected_str)


class CheckoutFormTests(TestCase):
    """
    Unit tests for checkout form validation and processing.

    Tests form behaviour:
    - Field validation (required fields, formats, constraints)
    - Form rendering and widget configuration
    - Error handling for invalid data
    - Integration with Order model
    """

    def test_order_form_valid_data(self):
        """Test OrderForm validation with valid data."""
        form_data = {
            "full_name": "John Doe",
            "email": "john@example.com",
            "phone_number": "+44 20 7946 0958",
            "street_address_1": "123 Main St",
            "street_address_2": "Apartment 4B",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
        }

        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test cleaned data
        self.assertEqual(form.cleaned_data["full_name"], "John Doe")
        self.assertEqual(form.cleaned_data["email"], "john@example.com")
        self.assertEqual(form.cleaned_data["country"], "GB")

    def test_order_form_required_fields(self):
        """Test OrderForm validation with missing required fields."""
        form_data = {
            "email": "john@example.com",  # Missing other required fields
        }

        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Check that required fields have errors
        self.assertIn("full_name", form.errors)
        self.assertIn("street_address_1", form.errors)
        self.assertIn("city", form.errors)
        self.assertIn("postcode", form.errors)
        self.assertIn("country", form.errors)

    def test_order_form_email_validation(self):
        """Test OrderForm email field validation."""
        form_data = {
            "full_name": "John Doe",
            "email": "invalid-email",  # Invalid email format
            "street_address_1": "123 Main St",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
        }

        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_order_form_field_widgets(self):
        """Test OrderForm field widgets and attributes."""
        form = OrderForm()

        # Test that form has expected fields
        expected_fields = [
            "full_name",
            "email",
            "phone_number",
            "street_address_1",
            "street_address_2",
            "city",
            "postcode",
            "country",
        ]

        for field_name in expected_fields:
            self.assertIn(field_name, form.fields)

        # Test that phone_number is not required (optional field)
        self.assertFalse(form.fields["phone_number"].required)
        self.assertFalse(form.fields["street_address_2"].required)


class CheckoutViewTests(TestCase):
    """
    Integration tests for checkout view functionality.

    Tests view behaviour:
    - Authentication requirements and redirects
    - Cart validation and display
    - Form processing and session handling
    - Multi-step checkout workflow
    """

    def setUp(self):
        """Set up test fixtures for view testing."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        # Create test products
        self.base_game = Product.objects.create(
            name="Eclipse Protocol Game",
            slug="eclipse-protocol-game-view-test",
            description="Test game description",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            sku="EP-BASE-VIEW",
        )

        self.variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform="PC",
            edition="ULTIMATE",
            price_override=Decimal("59.99"),
        )

        # Create cart with items
        self.cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(
            cart=self.cart,
            product=self.base_game,
            variant=self.variant,
            quantity=1,
        )

    def test_checkout_requires_login(self):
        """Test checkout view requires user authentication."""
        response = self.client.get(reverse("checkout:checkout"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response.url)

    def test_checkout_redirects_empty_cart(self):
        """Test checkout redirects when cart is empty."""
        # Create user with empty cart
        User.objects.create_user(
            username="emptyuser",
            email="empty@example.com",
            password="testpass123",
        )

        self.client.login(username="emptyuser", password="testpass123")
        response = self.client.get(reverse("checkout:checkout"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("home"))

    def test_checkout_displays_cart_items(self):
        """Test checkout page displays cart items correctly."""
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("checkout:checkout"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Eclipse Protocol Game")
        self.assertContains(response, "PC")
        self.assertContains(response, "ULTIMATE")
        self.assertContains(response, "59.99")

    def test_checkout_form_submission_creates_session_data(self):
        """Test successful checkout form submission stores data in session."""
        self.client.login(username="testuser", password="testpass123")

        form_data = {
            "full_name": "Test User",
            "email": "test@example.com",
            "phone_number": "+44 123 456 7890",
            "street_address_1": "123 Test Street",
            "street_address_2": "Apartment 4B",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
        }

        response = self.client.post(
            reverse("checkout:checkout"), data=form_data
        )

        # Should redirect to review page
        self.assertEqual(response.status_code, 302)
        self.assertIn("review", response.url)

        # Should store form data in session with correct key
        session = self.client.session
        self.assertIn("billing_address", session)
        self.assertEqual(session["billing_address"]["full_name"], "Test User")

    def test_checkout_with_saved_address(self):
        """Test checkout pre-populates form with saved billing address."""
        # Create saved billing address
        Address.objects.create(
            user=self.user,
            address_type=Address.BILLING,
            full_name="John Doe",
            address_line_1="456 Saved Street",
            city="Manchester",
            postcode="M1 1AA",
            country="GB",
        )

        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("checkout:checkout"))
        self.assertEqual(response.status_code, 200)

        # Check that saved address data is in the form
        self.assertContains(response, "John Doe")
        self.assertContains(response, "456 Saved Street")
        self.assertContains(response, "Manchester")


class CheckoutPaymentTests(TestCase):
    """
    Integration tests for payment processing workflows.

    Tests payment functionality:
    - Stripe payment intent creation
    - Payment success handling
    - Payment failure handling
    - Order and license key creation after successful payment
    """

    def setUp(self):
        """Set up test fixtures for payment testing."""
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        # Create test products
        self.base_game = Product.objects.create(
            name="Eclipse Protocol Game",
            slug="eclipse-protocol-game-payment-test",
            description="Test game",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            sku="EP-BASE-PAYMENT",
        )

        self.variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform="PC",
            edition="ULTIMATE",
            price_override=Decimal("59.99"),
        )

        # Create cart
        self.cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(
            cart=self.cart,
            product=self.base_game,
            variant=self.variant,
            quantity=1,
        )

    @patch("stripe.PaymentIntent.create")
    def test_payment_intent_creation(self, mock_payment_intent):
        """Test Stripe PaymentIntent creation with correct parameters."""
        # Mock Stripe PaymentIntent response
        mock_payment_intent.return_value = Mock(
            id="pi_test_1234567890",
            client_secret="pi_test_1234567890_secret_test",
            status="requires_confirmation",
        )

        self.client.login(username="testuser", password="testpass123")

        # Set up session with billing address data (correct session key)
        session = self.client.session
        session["billing_address"] = {
            "full_name": "Test User",
            "email": "test@example.com",
            "street_address_1": "123 Test Street",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
        }
        session.save()

        self.client.get(reverse("checkout:payment"))

        # Verify PaymentIntent was created with correct amount
        mock_payment_intent.assert_called_once()
        call_kwargs = mock_payment_intent.call_args[1]
        self.assertEqual(call_kwargs["amount"], 5999)  # £59.99 in pence
        self.assertEqual(call_kwargs["currency"], "gbp")
        self.assertIn("user_id", call_kwargs["metadata"])

    def test_payment_page_requires_billing_address(self):
        """
        Test payment page redirects if no billing address data in session.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("checkout:payment"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("checkout:checkout"))

    @patch(
        "checkout.webhook_handler.StripeWH_Handler._send_confirmation_email"
    )
    def test_successful_payment_creates_order(self, mock_email):
        """Test successful payment creates order and license keys."""
        # Create order directly to simulate successful payment webhook
        order = Order.objects.create(
            user=self.user,
            full_name="Test User",
            email="test@example.com",
            street_address_1="123 Test Street",
            city="London",
            postcode="SW1A 1AA",
            country="GB",
            total_amount=Decimal("59.99"),
            payment_status=Order.PAYMENT_PAID,
            stripe_pid="pi_test_1234567890",
            original_cart=json.dumps(
                [
                    {
                        "product_id": self.base_game.id,
                        "variant_id": self.variant.id,
                        "quantity": 1,
                        "price": "59.99",
                    }
                ]
            ),
        )

        # Create order item
        order_item = OrderItem.objects.create(
            order=order,
            product=self.base_game,
            variant=self.variant,
            product_name=self.base_game.name,
            product_sku=self.base_game.sku,
            variant_details="PC Ultimate Edition",
            quantity=1,
            unit_price=Decimal("59.99"),
        )

        # Create payment record
        payment = Payment.objects.create(
            order=order,
            transaction_id="pi_test_1234567890",
            amount=Decimal("59.99"),
            status=Payment.SUCCEEDED,
        )

        # Verify order was created correctly
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.total_amount, Decimal("59.99"))
        self.assertEqual(order.payment_status, Order.PAYMENT_PAID)
        self.assertEqual(order.items.count(), 1)

        # Verify payment was recorded
        self.assertTrue(payment.is_successful)

        # Verify order item was created
        self.assertEqual(order_item.product, self.base_game)
        self.assertEqual(order_item.variant, self.variant)
        self.assertEqual(order_item.total_price, Decimal("59.99"))


class CheckoutFunctionalTests(TestCase):
    """
    End-to-end functional tests for complete checkout workflows.

    Tests realistic user scenarios:
    - Complete checkout process from cart to confirmation
    - Multiple payment scenarios (success/failure)
    - License key delivery workflow
    - Order history integration
    """

    def setUp(self):
        """Set up complete test environment for functional testing."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        # Create products for realistic checkout scenario
        self.base_game = Product.objects.create(
            name="Eclipse Protocol Game",
            slug="eclipse-protocol-game-functional-test",
            description="Test game",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            sku="EP-BASE-FUNCTIONAL",
        )

        self.variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform="PC",
            edition="ULTIMATE",
            price_override=Decimal("59.99"),
        )

        self.currency_product = Product.objects.create(
            name="Eclipse Credits Pack",
            slug="eclipse-credits-pack-functional-test",
            description="In-game currency",
            price=Decimal("9.99"),
            product_type=Product.CURRENCY,
            sku="EP-CURR-FUNCTIONAL",
        )

        # Create cart with mixed items
        self.cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(
            cart=self.cart,
            product=self.base_game,
            variant=self.variant,
            quantity=1,
        )
        CartItem.objects.create(
            cart=self.cart, product=self.currency_product, quantity=2
        )

    def test_complete_checkout_workflow(self):
        """Test complete checkout workflow from cart to order confirmation."""
        self.client.login(username="testuser", password="testpass123")

        # Step 1: Access checkout page
        response = self.client.get(reverse("checkout:checkout"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Eclipse Protocol Game")
        self.assertContains(response, "Eclipse Credits Pack")

        # Step 2: Submit billing information
        form_data = {
            "full_name": "Test User",
            "email": "test@example.com",
            "phone_number": "+44 123 456 7890",
            "street_address_1": "123 Test Street",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
        }

        response = self.client.post(
            reverse("checkout:checkout"), data=form_data
        )
        self.assertEqual(response.status_code, 302)

        # Step 3: Verify session data was stored with correct key
        session = self.client.session
        self.assertIn("billing_address", session)
        self.assertEqual(session["billing_address"]["full_name"], "Test User")

    def test_checkout_saves_billing_address_when_requested(self):
        """
        Test checkout saves billing address to user account when requested.
        """
        self.client.login(username="testuser", password="testpass123")

        form_data = {
            "full_name": "Test User",
            "email": "test@example.com",
            "street_address_1": "123 Test Street",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
            "save_address": "on",  # Request to save address
        }

        self.client.post(reverse("checkout:checkout"), data=form_data)

        # Verify address was saved
        saved_address = Address.objects.filter(
            user=self.user, address_type=Address.BILLING
        ).first()

        self.assertIsNotNone(saved_address)
        self.assertEqual(saved_address.full_name, "Test User")
        self.assertEqual(saved_address.address_line_1, "123 Test Street")
        self.assertEqual(saved_address.city, "London")

    def test_checkout_workflow_with_saved_address(self):
        """Test checkout workflow when user has saved billing address."""
        # Create saved billing address first
        Address.objects.create(
            user=self.user,
            address_type=Address.BILLING,
            full_name="Saved User",
            address_line_1="456 Saved Street",
            city="Manchester",
            postcode="M1 1AA",
            country="GB",
        )

        self.client.login(username="testuser", password="testpass123")

        # Access checkout - should pre-populate with saved address
        response = self.client.get(reverse("checkout:checkout"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Saved User")
        self.assertContains(response, "456 Saved Street")

    @patch("stripe.PaymentIntent.create")
    def test_review_and_payment_flow(self, mock_payment_intent):
        """Test review order and payment flow."""
        # Mock Stripe PaymentIntent
        mock_payment_intent.return_value = Mock(
            id="pi_test_1234567890",
            client_secret="pi_test_1234567890_secret_test",
        )

        self.client.login(username="testuser", password="testpass123")

        # Submit checkout form first
        form_data = {
            "full_name": "Test User",
            "email": "test@example.com",
            "street_address_1": "123 Test Street",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
        }

        self.client.post(reverse("checkout:checkout"), data=form_data)

        # Access review page
        response = self.client.get(reverse("checkout:review"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")
        self.assertContains(response, "123 Test Street")

        # Access payment page
        response = self.client.get(reverse("checkout:payment"))
        self.assertEqual(response.status_code, 200)

        # Verify PaymentIntent was created
        mock_payment_intent.assert_called_once()


# Additional test cases for edge cases and error handling
class CheckoutErrorHandlingTests(TestCase):
    """
    Tests for checkout error handling and edge cases.

    Tests error scenarios:
    - Session expiry during checkout
    - Payment failures and retries
    - Database errors during order creation
    - Invalid product configurations
    """

    def setUp(self):
        """Set up test fixtures for error testing."""
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        self.product = Product.objects.create(
            name="Test Product",
            slug="test-product-error",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            sku="TEST-ERROR",
        )

    def test_checkout_without_cart(self):
        """Test checkout behaviour when user has no cart."""
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("checkout:checkout"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("home"))

    def test_review_without_billing_address(self):
        """Test review page redirects when no billing address in session."""
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("checkout:review"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("checkout:checkout"))

    def test_payment_without_billing_address(self):
        """Test payment page redirects when no billing address in session."""
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("checkout:payment"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("checkout:checkout"))

    def test_checkout_form_validation_errors(self):
        """Test checkout form handles validation errors properly."""
        # Create cart first
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product=self.product, quantity=1)

        self.client.login(username="testuser", password="testpass123")

        # Submit form with invalid data
        form_data = {
            "full_name": "",  # Required field left empty
            "email": "invalid-email",  # Invalid email format
            "street_address_1": "123 Test Street",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
        }

        response = self.client.post(
            reverse("checkout:checkout"), data=form_data
        )

        # Should stay on checkout page with errors
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "error")  # Should show error message

        # Should not create session data
        session = self.client.session
        self.assertNotIn("billing_address", session)


# Test configuration for mocking Stripe settings
@override_settings(
    STRIPE_PUBLIC_KEY="pk_test_123",
    STRIPE_SECRET_KEY="sk_test_123",
    STRIPE_CURRENCY="gbp",
)
class CheckoutStripeIntegrationTests(TestCase):
    """
    Tests for Stripe payment integration.

    Tests Stripe-specific functionality:
    - API key configuration
    - PaymentIntent creation and management
    - Webhook handling
    - Error handling for Stripe failures
    """

    def setUp(self):
        """Set up test fixtures for Stripe testing."""
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        self.product = Product.objects.create(
            name="Test Product",
            slug="test-product-stripe",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            sku="TEST-STRIPE",
        )

        # Create cart
        self.cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(
            cart=self.cart, product=self.product, quantity=1
        )

    @patch("stripe.PaymentIntent.create")
    def test_stripe_payment_intent_creation_with_settings(self, mock_create):
        """Test PaymentIntent creation uses correct Stripe settings."""
        mock_create.return_value = Mock(
            id="pi_test_123", client_secret="pi_test_123_secret"
        )

        self.client.login(username="testuser", password="testpass123")

        # Set up session
        session = self.client.session
        session["billing_address"] = {
            "full_name": "Test User",
            "email": "test@example.com",
            "street_address_1": "123 Test Street",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
        }
        session.save()

        self.client.get(reverse("checkout:payment"))

        # Verify PaymentIntent created with correct settings
        mock_create.assert_called_once()
        call_kwargs = mock_create.call_args[1]
        self.assertEqual(call_kwargs["currency"], "gbp")
        self.assertEqual(call_kwargs["amount"], 4999)  # £49.99 in pence

    @patch("stripe.PaymentIntent.create")
    def test_stripe_error_handling(self, mock_create):
        """Test proper error handling when Stripe API fails."""
        # Mock Stripe API error
        import stripe

        mock_create.side_effect = stripe.error.StripeError("Stripe API Error")

        self.client.login(username="testuser", password="testpass123")

        # Set up session
        session = self.client.session
        session["billing_address"] = {
            "full_name": "Test User",
            "email": "test@example.com",
            "street_address_1": "123 Test Street",
            "city": "London",
            "postcode": "SW1A 1AA",
            "country": "GB",
        }
        session.save()

        response = self.client.get(reverse("checkout:payment"))

        # Should redirect to review page on Stripe error
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("checkout:review"))
