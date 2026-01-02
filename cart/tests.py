import json
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from catalog.models import CurrencyProduct, DigitalVariant, Product

from .context_processors import cart_contents
from .models import Cart, CartItem


class CartModelTests(TestCase):
    """
    Unit tests for Cart and CartItem model functionality.

    These tests verify the core business logic of cart models:
    - Cart creation and string representation
    - Item counting and total price calculations
    - CartItem relationships and properties
    - Database constraint enforcement
    """

    def setUp(self):
        """
        Set up test fixtures: user, products, and variants for cart testing.
        """
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        # Create base game product for testing variants
        self.base_game = Product.objects.create(
            name="Eclipse Protocol Game",
            slug="eclipse-protocol-game-model-test",
            description="Test game",
            price=Decimal("49.99"),
            product_type="base_game",
            sku="EP-BASE-001",
        )

        # Create variant with price override for testing pricing logic
        self.variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform="PC",
            edition="ULTIMATE",
            price_override=Decimal("59.99"),
        )

        # Create currency product for testing simple product handling
        self.currency_product = Product.objects.create(
            name="Eclipse Credits Pack",
            slug="eclipse-credits-pack-model-test",
            description="In-game currency",
            price=Decimal("9.99"),
            product_type="currency",
            sku="EP-CURR-001",
        )

        # Use get_or_create to avoid conflicts with post_save signal
        CurrencyProduct.objects.get_or_create(
            product=self.currency_product, defaults={"credit_amount": 1000}
        )

    def test_cart_creation(self):
        """Test cart model creation and string representation."""
        cart = Cart.objects.create(user=self.user)
        self.assertEqual(cart.user, self.user)
        self.assertEqual(str(cart), f"Cart for {self.user.username}")

    def test_cart_total_items_empty(self):
        """
        Test that empty cart returns 0 for total_items property.
        """
        cart = Cart.objects.create(user=self.user)
        self.assertEqual(cart.total_items, 0)

    def test_cart_total_items_with_items(self):
        """
        Test total_items property correctly sums quantities
        across all cart items.
        """
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(
            cart=cart, product=self.base_game, variant=self.variant, quantity=2
        )
        CartItem.objects.create(
            cart=cart, product=self.currency_product, quantity=3
        )

        self.assertEqual(cart.total_items, 5)  # 2 + 3 = 5

    def test_cart_total_price_empty(self):
        """Test that empty cart returns 0 for total_price property."""
        cart = Cart.objects.create(user=self.user)
        self.assertEqual(cart.total_price, 0)

    def test_cart_total_price_with_items(self):
        """
        Test total_price property correctly calculates sum of line totals
        """
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(
            cart=cart, product=self.base_game, variant=self.variant, quantity=1
        )
        CartItem.objects.create(
            cart=cart, product=self.currency_product, quantity=2
        )

        # £59.99 (variant price) + £9.99 * 2 = £79.97
        expected_total = Decimal("59.99") + (Decimal("9.99") * 2)
        self.assertEqual(cart.total_price, expected_total)

    def test_cart_item_creation(self):
        """Test cart item model creation with all required relationships."""
        cart = Cart.objects.create(user=self.user)
        item = CartItem.objects.create(
            cart=cart, product=self.base_game, variant=self.variant, quantity=1
        )

        # Verify all relationships are set correctly
        self.assertEqual(item.cart, cart)
        self.assertEqual(item.product, self.base_game)
        self.assertEqual(item.variant, self.variant)
        self.assertEqual(item.quantity, 1)

    def test_cart_item_string_representation(self):
        """
        Test cart item __str__ method handles variant and non-variant products
        """
        cart = Cart.objects.create(user=self.user)

        # Test with variant (should include variant info)
        item_with_variant = CartItem.objects.create(
            cart=cart, product=self.base_game, variant=self.variant, quantity=2
        )
        self.assertIn(self.base_game.name, str(item_with_variant))
        self.assertIn("x2", str(item_with_variant))

        # Test without variant (simple format)
        item_without_variant = CartItem.objects.create(
            cart=cart, product=self.currency_product, quantity=3
        )
        self.assertEqual(
            str(item_without_variant), f"{self.currency_product.name} x3"
        )

    def test_cart_item_effective_price_with_variant(self):
        """Test effective_price property uses variant price when available."""
        cart = Cart.objects.create(user=self.user)
        item = CartItem.objects.create(
            cart=cart, product=self.base_game, variant=self.variant, quantity=1
        )

        # Should use variant's price override (£59.99), not base price (£49.99)
        self.assertEqual(item.effective_price, Decimal("59.99"))

    def test_cart_item_effective_price_without_variant(self):
        """Test effective_price falls back to product price when no variant."""
        cart = Cart.objects.create(user=self.user)
        item = CartItem.objects.create(
            cart=cart, product=self.currency_product, quantity=1
        )

        # Should use base product price
        self.assertEqual(item.effective_price, Decimal("9.99"))

    def test_cart_item_line_total(self):
        """Test line_total multiplies effective price by quantity correctly."""
        cart = Cart.objects.create(user=self.user)
        item = CartItem.objects.create(
            cart=cart, product=self.currency_product, quantity=3
        )

        expected_line_total = Decimal("9.99") * 3
        self.assertEqual(item.line_total, expected_line_total)


class CartContextProcessorTests(TestCase):
    """
    Unit tests for cart_contents context processor.

    Tests the context processor that makes cart data available
    across templates.

    Verifies handling of:
    - Empty carts
    - Session cart data parsing
    - Product/variant lookups
    - Total calculations
    - Error handling for deleted products
    """

    def setUp(self):
        """
        Set up test fixtures and request factory for context processor testing
        """
        self.factory = RequestFactory()

        # Create test products for context processor testing
        self.base_game = Product.objects.create(
            name="Eclipse Protocol Game",
            slug="eclipse-protocol-game-context-test",
            description="Test game",
            price=Decimal("49.99"),
            product_type="base_game",
            sku="EP-BASE-002",
        )

        self.variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform="PC",
            edition="ULTIMATE",
            price_override=Decimal("59.99"),
        )

        self.currency_product = Product.objects.create(
            name="Eclipse Credits Pack",
            slug="eclipse-credits-pack-context-test",
            description="In-game currency",
            price=Decimal("9.99"),
            product_type="currency",
            sku="EP-CURR-002",
        )

    def test_empty_cart(self):
        """
        Test context processor returns correct empty state
        for requests without cart session.
        """
        request = self.factory.get("/")
        request.session = {}

        context = cart_contents(request)

        # Verify all cart totals are zero/empty
        self.assertEqual(context["cart_items"], [])
        self.assertEqual(context["total"], Decimal("0.00"))
        self.assertEqual(context["product_count"], 0)
        self.assertEqual(context["delivery"], Decimal("0.00"))
        self.assertEqual(context["grand_total"], Decimal("0.00"))
        self.assertFalse(context["shipping_required"])

    def test_cart_with_simple_product(self):
        """
        Test context processor correctly parses session cart with
        currency products.
        """
        request = self.factory.get("/")
        request.session = {
            "cart": {
                str(self.currency_product.id): {
                    "product_id": self.currency_product.id,
                    "quantity": 2,
                    "platform": "PC",
                }
            }
        }

        context = cart_contents(request)

        # Verify cart parsing and calculations
        self.assertEqual(len(context["cart_items"]), 1)
        self.assertEqual(context["product_count"], 2)
        self.assertEqual(context["total"], Decimal("9.99") * 2)
        self.assertEqual(context["grand_total"], Decimal("9.99") * 2)

    def test_cart_with_variant_product(self):
        """
        Test context processor handles products with variants in session cart
        """
        request = self.factory.get("/")
        request.session = {
            "cart": {
                f"{self.base_game.id}_{self.variant.id}": {
                    "product_id": self.base_game.id,
                    "variant_id": self.variant.id,
                    "quantity": 1,
                    "platform": "PC",
                }
            }
        }

        context = cart_contents(request)

        # Verify variant handling
        self.assertEqual(len(context["cart_items"]), 1)
        self.assertEqual(context["product_count"], 1)
        self.assertEqual(
            context["total"], Decimal("59.99")
        )  # Uses variant price

        cart_item = context["cart_items"][0]
        self.assertEqual(cart_item["product"], self.base_game)
        self.assertEqual(cart_item["variant"], self.variant)
        self.assertEqual(cart_item["price"], Decimal("59.99"))

    def test_cart_with_multiple_items(self):
        """
        Test context processor correctly handles mixed cart
        with multiple item types.
        """
        request = self.factory.get("/")
        request.session = {
            "cart": {
                str(self.currency_product.id): {
                    "product_id": self.currency_product.id,
                    "quantity": 3,
                    "platform": "PC",
                },
                f"{self.base_game.id}_{self.variant.id}": {
                    "product_id": self.base_game.id,
                    "variant_id": self.variant.id,
                    "quantity": 1,
                    "platform": "PC",
                },
            }
        }

        context = cart_contents(request)

        # Verify mixed cart calculations
        self.assertEqual(len(context["cart_items"]), 2)
        self.assertEqual(context["product_count"], 4)  # 3 + 1 = 4
        expected_total = (Decimal("9.99") * 3) + Decimal("59.99")
        self.assertEqual(context["total"], expected_total)

    def test_cart_handles_deleted_product_gracefully(self):
        """Test context processor skips invalid products without crashing."""
        request = self.factory.get("/")
        request.session = {
            "cart": {
                "9999": {  # Non-existent product ID
                    "product_id": 9999,
                    "quantity": 1,
                    "platform": "PC",
                },
                str(self.currency_product.id): {
                    "product_id": self.currency_product.id,
                    "quantity": 2,
                    "platform": "PC",
                },
            }
        }

        context = cart_contents(request)

        # Should only contain the valid product, invalid ones are skipped
        self.assertEqual(len(context["cart_items"]), 1)
        self.assertEqual(context["product_count"], 2)


class CartViewTests(TestCase):
    """
    Integration tests for cart views and AJAX endpoints.

    Tests the cart view functionality including:
    - Cart display for authenticated/anonymous users
    - Adding products to cart via AJAX
    - Handling variants and product types
    - Duplicate product prevention
    - Quantity increment logic
    """

    def setUp(self):
        """Set up test client, user, and products for view testing."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        # Create test products for view testing
        self.base_game = Product.objects.create(
            name="Eclipse Protocol Game",
            slug="eclipse-protocol-game-view-test",
            description="Test game",
            price=Decimal("49.99"),
            product_type="base_game",
            sku="EP-BASE-003",
        )

        self.variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform="PC",
            edition="ULTIMATE",
            price_override=Decimal("59.99"),
        )

        self.currency_product = Product.objects.create(
            name="Eclipse Credits Pack",
            slug="eclipse-credits-pack-view-test",
            description="In-game currency",
            price=Decimal("9.99"),
            product_type="currency",
            sku="EP-CURR-003",
        )

    def test_cart_view_anonymous_user(self):
        """
        Test cart page loads correctly for anonymous users using session cart.
        """
        response = self.client.get(reverse("cart:cart"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")
        self.assertEqual(response.context["total_items"], 0)

    def test_cart_view_authenticated_user(self):
        """
        Test cart page loads correctly for authenticated users
        using database cart.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("cart:cart"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")

    def test_add_to_cart_anonymous_user(self):
        """
        Test adding products to session cart for anonymous users via AJAX.
        """
        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.currency_product.id]),
            {"quantity": 2},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data["success"])
        self.assertIn("Eclipse Credits", data["message"])
        self.assertEqual(data["cart_total"], 2)

    def test_add_to_cart_authenticated_user(self):
        """
        Test adding products to database cart for authenticated
        users via AJAX.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.currency_product.id]),
            {"quantity": 3},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data["success"])
        self.assertEqual(data["cart_total"], 3)

        # Verify cart item was persisted in database
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)
        cart_item = cart.items.first()
        self.assertEqual(cart_item.product, self.currency_product)
        self.assertEqual(cart_item.quantity, 3)

    def test_add_to_cart_with_variant(self):
        """
        Test adding products with variants correctly links
        variant to cart item.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.base_game.id]),
            {"variant_id": self.variant.id, "quantity": 1},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data["success"])

        # Verify variant relationship in database
        cart = Cart.objects.get(user=self.user)
        cart_item = cart.items.first()
        self.assertEqual(cart_item.variant, self.variant)

    def test_add_duplicate_digital_product_fails(self):
        """
        Test that adding duplicate digital products is prevented
        (no quantity increment).
        """
        self.client.login(username="testuser", password="testpass123")

        # Add product first time
        self.client.post(
            reverse("cart:add_to_cart", args=[self.base_game.id]),
            {"variant_id": self.variant.id, "quantity": 1},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Try to add same product again - should fail
        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.base_game.id]),
            {"variant_id": self.variant.id, "quantity": 1},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data["success"])
        self.assertIn("already in your cart", data["message"])

    def test_add_currency_product_increments_quantity(self):
        """
        Test that adding duplicate currency products increments
        quantity (business rule).
        """
        self.client.login(username="testuser", password="testpass123")

        # Add product first time
        self.client.post(
            reverse("cart:add_to_cart", args=[self.currency_product.id]),
            {"quantity": 2},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Add same product again - should increment quantity
        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.currency_product.id]),
            {"quantity": 3},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data["success"])
        self.assertEqual(data["cart_total"], 5)  # 2 + 3 = 5

        # Verify quantity was incremented in database
        cart = Cart.objects.get(user=self.user)
        cart_item = cart.items.first()
        self.assertEqual(cart_item.quantity, 5)


class CartFunctionalTests(TestCase):
    """
    End-to-end functional tests for complete cart workflows.

    Tests realistic user scenarios from start to finish:
    - Complete shopping workflows for different user types
    - Multi-product carts with variants
    - Cart persistence across sessions
    - Business logic for different product types
    """

    def setUp(self):
        """
        Set up test client, user, and product catalog for functional testing
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        # Create complete product setup for realistic testing
        self.base_game = Product.objects.create(
            name="Eclipse Protocol Game",
            slug="eclipse-protocol-game-functional-test",
            description="Test game",
            price=Decimal("49.99"),
            product_type="base_game",
            sku="EP-BASE-004",
        )

        # Create multiple variants for testing variant handling
        self.variant_pc = DigitalVariant.objects.create(
            product=self.base_game,
            platform="PC",
            edition="ULTIMATE",
            price_override=Decimal("59.99"),
        )

        self.variant_xbox = DigitalVariant.objects.create(
            product=self.base_game,
            platform="XBOX",
            edition="STANDARD",
            price_override=Decimal("49.99"),
        )

        self.currency_product = Product.objects.create(
            name="Eclipse Credits Pack",
            slug="eclipse-credits-pack-functional-test",
            description="In-game currency",
            price=Decimal("9.99"),
            product_type="currency",
            sku="EP-CURR-004",
        )

    def test_complete_shopping_workflow_authenticated(self):
        """
        Test complete authenticated user shopping workflow:
          add products, view cart, verify persistence.
        """
        self.client.login(username="testuser", password="testpass123")

        # Step 1: Add base game with variant
        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.base_game.id]),
            {"variant_id": self.variant_pc.id, "quantity": 1},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertTrue(json.loads(response.content)["success"])

        # Step 2: Add currency product
        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.currency_product.id]),
            {"quantity": 2},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertTrue(json.loads(response.content)["success"])

        # Step 3: View cart page and verify display
        response = self.client.get(reverse("cart:cart"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["total_items"], 3
        )  # 1 game + 2 currency

        expected_total = Decimal("59.99") + (Decimal("9.99") * 2)
        self.assertEqual(response.context["total_price"], expected_total)

        # Step 4: Verify cart persistence in database
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 2)
        self.assertEqual(cart.total_items, 3)
        self.assertEqual(cart.total_price, expected_total)

    def test_complete_shopping_workflow_anonymous(self):
        """
        Test complete anonymous user shopping workflow using session cart.
        """
        # Step 1: Add products to session cart
        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.base_game.id]),
            {"variant_id": self.variant_pc.id, "quantity": 1},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertTrue(json.loads(response.content)["success"])

        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.currency_product.id]),
            {"quantity": 3},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertTrue(json.loads(response.content)["success"])

        # Step 2: View cart and verify session-based calculations
        response = self.client.get(reverse("cart:cart"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["total_items"], 4
        )  # 1 game + 3 currency

        expected_total = Decimal("59.99") + (Decimal("9.99") * 3)
        self.assertEqual(response.context["total_price"], expected_total)

    def test_multiple_variants_same_product(self):
        """
        Test adding different variants of the same base product
        creates separate cart items.
        """
        self.client.login(username="testuser", password="testpass123")

        # Add PC variant
        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.base_game.id]),
            {"variant_id": self.variant_pc.id, "quantity": 1},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertTrue(json.loads(response.content)["success"])

        # Add Xbox variant (different variant, same base product)
        response = self.client.post(
            reverse("cart:add_to_cart", args=[self.base_game.id]),
            {"variant_id": self.variant_xbox.id, "quantity": 1},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertTrue(json.loads(response.content)["success"])

        # Verify both variants are treated as separate items
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 2)  # Two separate cart items
        self.assertEqual(cart.total_items, 2)  # Total quantity

        # Verify different pricing is respected
        expected_total = Decimal("59.99") + Decimal(
            "49.99"
        )  # PC Ultimate + Xbox Standard
        self.assertEqual(cart.total_price, expected_total)
