from decimal import Decimal

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import Client, TestCase
from django.urls import reverse

from .models import (
    DigitalProduct,
    DigitalVariant,
    Product,
    Wishlist,
)

# =============================================================================
# UNIT TESTS
# =============================================================================
# Test individual methods/properties in isolation
# - Fast execution (minimal database operations)
# - Test single responsibility
# - (Similar to testing pure functions in Jest)
# =============================================================================


class ProductModelTests(TestCase):
    """Unit tests for Product model methods and properties"""

    def test_sku_auto_generation(self):
        """
        UNIT TEST: Test SKU generation logic

        Tests the save() method's SKU generation without testing
        any relationships or external dependencies.
        """
        base_game = Product.objects.create(
            name="Test Game",
            slug="test-game",
            description="Test description",
            price=Decimal("19.99"),
            product_type=Product.BASE_GAME,
        )
        self.assertTrue(base_game.sku.startswith("EP-BG-"))

        currency = Product.objects.create(
            name="Credits",
            slug="credits",
            description="Test credits",
            price=Decimal("9.99"),
            product_type=Product.CURRENCY,
        )
        self.assertTrue(currency.sku.startswith("EP-CR-"))

    def test_product_string_representation(self):
        """
        UNIT TEST: Test __str__ method

        Simple test of string representation method - pure function behavior.
        """
        product = Product.objects.create(
            name="Eclipse Protocol",
            slug="eclipse-protocol",
            description="Test game",
            price=Decimal("29.99"),
            product_type=Product.BASE_GAME,
        )
        self.assertEqual(str(product), "Eclipse Protocol (Base Game)")


class DigitalVariantUnitTests(TestCase):
    """Unit tests for DigitalVariant model properties and methods"""

    def setUp(self):
        """Set up test data - reused across multiple tests"""
        self.base_game = Product.objects.create(
            name="Eclipse Protocol",
            slug="eclipse-protocol",
            description="Sci-fi strategy game",
            price=Decimal("24.99"),
            product_type=Product.BASE_GAME,
        )

    def test_variant_sku_generation(self):
        """
        UNIT TEST: Test SKU generation for variants

        Tests the save() method logic that combines base SKU + platform +
        edition.
        """
        variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD,
        )

        expected_sku = f"{self.base_game.sku}-PC-STANDARD"
        self.assertEqual(variant.sku, expected_sku)

    def test_effective_price_base(self):
        """
        UNIT TEST: Test effective_price property (no override)

        Tests @property method when price_override is None - should return
        base price.
        """
        variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD,
        )

        self.assertEqual(variant.effective_price, self.base_game.price)

    def test_effective_price_override(self):
        """
        UNIT TEST: Test effective_price property (with override)

        Tests @property method when price_override is set - should return
        override.
        """
        variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.ULTIMATE,
            price_override=Decimal("49.99"),
        )

        self.assertEqual(variant.effective_price, Decimal("49.99"))

    def test_full_description_property(self):
        """
        UNIT TEST: Test full_description property

        Tests the string manipulation logic that combines base + variant
        descriptions.
        """
        variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.PREMIUM,
            description="Includes season pass and exclusive skins",
        )

        full_desc = variant.full_description
        self.assertIn(self.base_game.description, full_desc)
        self.assertIn("Premium Edition Includes:", full_desc)
        self.assertIn("season pass", full_desc)


# =============================================================================
# INTEGRATION TESTS
# =============================================================================
# Test how multiple components work together
# - Test signals, model relationships, business workflows
# - Slower than unit tests (more database operations)
# - Test "does the whole system work together?"
# =============================================================================


class ProductExtensionTests(TestCase):
    """Integration tests for automatic extension creation via signals"""

    def test_currency_product_auto_creation(self):
        """
        INTEGRATION TEST: Signal creates CurrencyProduct extension

        Tests that post_save signal correctly creates related model.
        Involves Product model + CurrencyProduct model + signal handler.
        """
        product = Product.objects.create(
            name="100 Credits",
            slug="100-credits",
            description="Credit pack",
            price=Decimal("4.99"),
            product_type=Product.CURRENCY,
        )

        self.assertTrue(hasattr(product, "currency"))
        self.assertEqual(product.currency.credit_amount, 0)  # Default value

    def test_digital_product_auto_creation(self):
        """
        INTEGRATION TEST: Signal creates DigitalProduct extension

        Tests integration between Product creation and DigitalProduct
        auto-creation.
        """
        product = Product.objects.create(
            name="DLC Pack",
            slug="dlc-pack",
            description="Extra content",
            price=Decimal("7.99"),
            product_type=Product.DIGITAL,
        )

        self.assertTrue(hasattr(product, "digital"))
        self.assertTrue(product.digital.requires_key)  # Default value

    def test_base_game_no_auto_extension(self):
        """
        INTEGRATION TEST: Base games don't get auto-extensions

        Tests that signal correctly ignores BASE_GAME products.
        Verifies the conditional logic in the signal works.
        """
        product = Product.objects.create(
            name="Base Game",
            slug="base-game",
            description="Main game",
            price=Decimal("39.99"),
            product_type=Product.BASE_GAME,
        )

        with self.assertRaises(DigitalProduct.DoesNotExist):
            _ = product.digital


class WishlistIntegrationTests(TestCase):
    """Integration tests for wishlist functionality"""

    def setUp(self):
        """Set up User and Product for relationship testing"""
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.product = Product.objects.create(
            name="Wishlist Game",
            slug="wishlist-game",
            description="Game for wishlist testing",
            price=Decimal("19.99"),
            product_type=Product.BASE_GAME,
        )

    def test_wishlist_creation(self):
        """
        INTEGRATION TEST: Wishlist model relationships

        Tests that Wishlist correctly links User + Product models
        and handles timestamp creation.
        """
        wishlist = Wishlist.objects.create(
            user=self.user, product=self.product
        )

        self.assertEqual(wishlist.user, self.user)
        self.assertEqual(wishlist.product, self.product)
        self.assertIsNotNone(wishlist.added_at)

    def test_wishlist_uniqueness(self):
        """
        INTEGRATION TEST: Database constraint enforcement

        Tests that database-level unique_together constraint works correctly.
        Involves model + database constraint validation.
        """
        Wishlist.objects.create(
            user=self.user, product=self.product, variant=None
        )

        with self.assertRaises(IntegrityError):  # IntegrityError from database
            Wishlist.objects.create(
                user=self.user, product=self.product, variant=None
            )


class DigitalVariantIntegrationTests(TestCase):
    """Integration tests for variant-product relationships"""

    def setUp(self):
        self.base_game = Product.objects.create(
            name="Eclipse Protocol",
            slug="eclipse-protocol",
            description="Sci-fi strategy game",
            price=Decimal("24.99"),
            product_type=Product.BASE_GAME,
        )

    def test_variant_uniqueness(self):
        """
        INTEGRATION TEST: Database constraint on variant uniqueness

        Tests unique_together constraint on (product, platform, edition).
        Involves DigitalVariant model + database constraint validation.
        """
        DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD,
        )

        with self.assertRaises(Exception):  # IntegrityError from database
            DigitalVariant.objects.create(
                product=self.base_game,
                platform=DigitalProduct.PC,
                edition=DigitalProduct.STANDARD,
            )


# =============================================================================
# FUNCTIONAL TESTS
# =============================================================================
# Test complete user workflows from start to finish
# - Test admin interface accessibility (UI testing)
# - Test complete business processes
# =============================================================================


class ProductAdminTests(TestCase):
    """Functional tests for admin interface accessibility"""

    def setUp(self):
        """Set up admin user and client for UI testing"""
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpass123",
        )
        self.client = Client()
        self.client.login(username="admin", password="adminpass123")

    def test_product_admin_accessible(self):
        """
        FUNCTIONAL TEST: Admin pages load without crashing

        Tests that admin views render correctly - simulates real user clicking
        through admin interface. Tests Django admin + your admin
        customizations.
        """
        response = self.client.get("/admin/catalog/product/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/admin/catalog/product/add/")
        self.assertEqual(response.status_code, 200)

    def test_variant_admin_accessible(self):
        """
        FUNCTIONAL TEST: Variant admin accessibility

        Ensures your custom DigitalVariant admin interface works.
        """
        response = self.client.get("/admin/catalog/digitalvariant/")
        self.assertEqual(response.status_code, 200)

    def test_currency_admin_accessible(self):
        """
        FUNCTIONAL TEST: Currency admin accessibility

        Tests that CurrencyProduct admin with custom display methods works.
        """
        response = self.client.get("/admin/catalog/currencyproduct/")
        self.assertEqual(response.status_code, 200)


class ProductTypeWorkflowTests(TestCase):
    """Functional tests for complete product management workflows"""

    def test_base_game_workflow(self):
        """
        FUNCTIONAL TEST: Complete base game setup workflow

        Tests the entire process an admin would follow:
        1. Create base game product
        2. Add multiple variants
        3. Verify pricing works correctly

        This simulates real-world usage patterns.
        """
        # Step 1: Admin creates base game
        base_game = Product.objects.create(
            name="Eclipse Protocol",
            slug="eclipse-protocol",
            description="Strategy game",
            price=Decimal("29.99"),
            product_type=Product.BASE_GAME,
        )

        # Step 2: Admin adds variants for different platforms/editions
        pc_standard = DigitalVariant.objects.create(
            product=base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD,
        )

        pc_ultimate = DigitalVariant.objects.create(
            product=base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.ULTIMATE,
            price_override=Decimal("59.99"),
            description="Includes all DLC and season pass",
        )

        # Step 3: Verify the complete setup works correctly
        self.assertEqual(base_game.digital_variants.count(), 2)
        self.assertEqual(
            pc_standard.effective_price, Decimal("29.99")
        )  # Uses base price
        self.assertEqual(
            pc_ultimate.effective_price, Decimal("59.99")
        )  # Uses override

    def test_currency_workflow(self):
        """
        FUNCTIONAL TEST: Complete currency product setup

        Tests the workflow for creating credit packs - Product creation
        triggers signal, admin updates credit amount, system works end-to-end.
        """
        # Step 1: Admin creates currency product
        # (signal auto-creates extension)
        currency = Product.objects.create(
            name="500 Credits",
            slug="500-credits",
            description="In-game currency",
            price=Decimal("9.99"),
            product_type=Product.CURRENCY,
        )

        # Step 2: Admin configures credit amount
        currency.currency.credit_amount = 500
        currency.currency.save()

        # Step 3: Verify complete setup
        self.assertEqual(currency.currency.credit_amount, 500)
        self.assertEqual(str(currency.currency), "500 Credits")

    def test_digital_product_workflow(self):
        """
        FUNCTIONAL TEST: Complete digital product setup

        Tests workflow for simple digital products (DLC) - creation,
        configuration, and final verification.
        """
        # Step 1: Admin creates digital product (signal auto-creates extension)
        dlc = Product.objects.create(
            name="Expansion Pack",
            slug="expansion-pack",
            description="Extra content",
            price=Decimal("14.99"),
            product_type=Product.DIGITAL,
        )

        # Step 2: Admin configures platform/edition details
        dlc.digital.platform = DigitalProduct.PC
        dlc.digital.edition = DigitalProduct.STANDARD
        dlc.digital.save()

        # Step 3: Verify complete configuration
        self.assertEqual(dlc.digital.platform, DigitalProduct.PC)
        self.assertTrue(dlc.digital.requires_key)


class CatalogViewTests(TestCase):
    """Tests for catalog views and URL routing"""

    def setUp(self):
        """Set up test data for view testing"""
        self.client = Client()

        # Create base game with variants
        self.base_game = Product.objects.create(
            name="Eclipse Protocol",
            slug="eclipse-protocol",
            description="Sci-fi strategy game with immersive gameplay",
            price=Decimal("29.99"),
            product_type=Product.BASE_GAME,
            is_active=True,
        )

        # Create variants for testing edition_detail view
        self.pc_standard = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD,
            is_active=True,
        )

        self.pc_ultimate = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.ULTIMATE,
            price_override=Decimal("59.99"),
            description="Includes season pass and exclusive content",
            is_active=True,
        )

        self.xbox_standard = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.XBOX,
            edition=DigitalProduct.STANDARD,
            is_active=True,
        )

        # Create currency products for testing currency_detail view
        self.currency_100 = Product.objects.create(
            name="100 Eclipse Credits",
            slug="100-credits",
            description="Small credit pack",
            price=Decimal("4.99"),
            product_type=Product.CURRENCY,
            is_active=True,
        )

        self.currency_500 = Product.objects.create(
            name="500 Eclipse Credits",
            slug="500-credits",
            description="Medium credit pack",
            price=Decimal("19.99"),
            product_type=Product.CURRENCY,
            is_active=True,
        )

        # Create inactive product for testing filtering
        self.inactive_product = Product.objects.create(
            name="Discontinued Game",
            slug="discontinued-game",
            description="Old game",
            price=Decimal("39.99"),
            product_type=Product.BASE_GAME,
            is_active=False,
        )

    def test_currency_detail_view_default(self):
        """Test currency_detail view without specific product selection"""
        response = self.client.get(reverse("catalog:currency_detail"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/currency_detail.html")

        # Check context data
        self.assertEqual(len(response.context["currency_products"]), 2)
        self.assertEqual(
            response.context["page_info"]["name"], "Eclipse Protocol Credits"
        )
        self.assertIsNone(response.context["selected_product"])

        # Verify products are ordered by price
        products = list(response.context["currency_products"])
        self.assertEqual(products[0], self.currency_100)  # Cheaper first
        self.assertEqual(products[1], self.currency_500)

    def test_currency_detail_view_with_selection(self):
        """Test currency_detail view with specific product selected"""
        response = self.client.get(
            reverse(
                "catalog:currency_detail_with_selection",
                kwargs={"product_slug": "500-credits"},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["selected_product"], self.currency_500
        )
        self.assertEqual(
            response.context["page_info"]["name"], "500 Eclipse Credits"
        )
        self.assertEqual(
            response.context["page_info"]["description"], "Medium credit pack"
        )

    def test_currency_detail_view_invalid_slug(self):
        """Test currency_detail view with non-existent product slug"""
        response = self.client.get(
            reverse(
                "catalog:currency_detail_with_selection",
                kwargs={"product_slug": "non-existent"},
            )
        )

        self.assertEqual(response.status_code, 200)
        # Should fall back to default page info
        self.assertEqual(
            response.context["page_info"]["name"], "Eclipse Protocol Credits"
        )
        self.assertIsNone(response.context["selected_product"])

    def test_edition_detail_view_default_variant(self):
        """Test edition_detail view without specific platform/edition"""
        response = self.client.get(
            reverse(
                "catalog:edition_detail",
                kwargs={"product_slug": "eclipse-protocol"},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/edition_detail.html")

        # Check context data
        self.assertEqual(response.context["base_product"], self.base_game)
        # First variant
        self.assertEqual(
            response.context["selected_variant"], self.pc_standard
        )
        # All active variants
        self.assertEqual(len(response.context["variants"]), 3)

        # Check platform and edition organization
        self.assertIn("pc", response.context["variants_by_platform"])
        self.assertIn("xbox", response.context["variants_by_platform"])
        self.assertEqual(len(response.context["platforms"]), 2)
        self.assertIn("standard", response.context["editions"])
        self.assertIn("ultimate", response.context["editions"])

    def test_edition_detail_view_specific_variant(self):
        """Test edition_detail view with specific platform/edition selection"""
        response = self.client.get(
            reverse(
                "catalog:edition_detail_variant",
                kwargs={
                    "product_slug": "eclipse-protocol",
                    "platform": "pc",
                    "edition": "ultimate",
                },
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["selected_variant"], self.pc_ultimate
        )
        self.assertEqual(
            response.context["selected_variant"].effective_price,
            Decimal("59.99"),
        )

    def test_edition_detail_view_invalid_variant(self):
        """
        Test edition_detail view with invalid platform/edition combination
        """
        response = self.client.get(
            reverse(
                "catalog:edition_detail_variant",
                kwargs={
                    "product_slug": "eclipse-protocol",
                    "platform": "playstation",  # Doesn't exist
                    "edition": "standard",
                },
            )
        )

        self.assertEqual(response.status_code, 200)
        # Should fall back to first available variant
        self.assertEqual(
            response.context["selected_variant"], self.pc_standard
        )

    def test_edition_detail_view_nonexistent_product(self):
        """Test edition_detail view with non-existent product returns 404"""
        response = self.client.get(
            reverse(
                "catalog:edition_detail",
                kwargs={"product_slug": "non-existent-game"},
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_edition_detail_view_inactive_product(self):
        """Test edition_detail view with inactive product returns 404"""
        response = self.client.get(
            reverse(
                "catalog:edition_detail",
                kwargs={"product_slug": "discontinued-game"},
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_search_results_view_empty_query(self):
        """Test search_results view with no search query"""
        response = self.client.get(reverse("catalog:search_results"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/search_results.html")
        self.assertEqual(response.context["query"], "")
        self.assertEqual(len(response.context["products"]), 0)
        self.assertEqual(response.context["total_count"], 0)

    def test_search_results_view_with_query(self):
        """Test search_results view with search query"""
        response = self.client.get(
            reverse("catalog:search_results") + "?q=Eclipse"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["query"], "Eclipse")
        # base_game + 2 currency
        self.assertEqual(response.context["total_count"], 3)

        # Verify correct products returned
        products = list(response.context["products"])
        product_names = [p.name for p in products]
        self.assertIn("Eclipse Protocol", product_names)
        self.assertIn("100 Eclipse Credits", product_names)
        self.assertIn("500 Eclipse Credits", product_names)

    def test_search_results_view_description_match(self):
        """Test search_results view finds matches in description"""
        response = self.client.get(
            reverse("catalog:search_results") + "?q=strategy"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_count"], 1)
        self.assertEqual(list(response.context["products"])[0], self.base_game)

    def test_search_results_view_no_matches(self):
        """Test search_results view with query that matches nothing"""
        response = self.client.get(
            reverse("catalog:search_results") + "?q=nonexistent"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_count"], 0)
        self.assertEqual(len(response.context["products"]), 0)

    def test_search_results_view_case_insensitive(self):
        """Test search_results view is case-insensitive"""
        response = self.client.get(
            reverse("catalog:search_results") + "?q=ECLIPSE"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_count"], 3)

    def test_search_results_view_excludes_inactive(self):
        """Test search_results view excludes inactive products"""
        response = self.client.get(
            reverse("catalog:search_results") + "?q=Discontinued"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_count"], 0)


class CatalogViewEdgeCaseTests(TestCase):
    """Test edge cases and error conditions in catalog views"""

    def test_currency_detail_view_no_currency_products(self):
        """Test currency_detail view when no currency products exist"""
        response = self.client.get(reverse("catalog:currency_detail"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["currency_products"]), 0)
        self.assertEqual(
            response.context["page_info"]["name"], "Eclipse Protocol Credits"
        )
        self.assertIsNone(response.context["page_info"]["image"])

    def test_edition_detail_view_no_variants(self):
        """Test edition_detail view for base game with no variants"""
        base_game = Product.objects.create(
            name="No Variants Game",
            slug="no-variants-game",
            description="Game without variants",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            is_active=True,
        )

        response = self.client.get(
            reverse(
                "catalog:edition_detail",
                kwargs={"product_slug": "no-variants-game"},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["base_product"], base_game)
        self.assertIsNone(response.context["selected_variant"])
        self.assertEqual(len(response.context["variants"]), 0)

    def test_currency_detail_view_with_image(self):
        """Test currency_detail view properly handles product images"""
        # Create currency product with image
        from django.core.files.storage import default_storage
        from django.core.files.uploadedfile import SimpleUploadedFile

        # Mock image file
        image_content = b"fake-image-content"
        image_file = SimpleUploadedFile(
            "test.jpg", image_content, content_type="image/jpeg"
        )

        currency_with_image = Product.objects.create(
            name="Premium Credits",
            slug="premium-credits",
            description="Premium credit pack",
            price=Decimal("9.99"),
            product_type=Product.CURRENCY,
            is_active=True,
            image=image_file,
        )

        response = self.client.get(reverse("catalog:currency_detail"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["page_info"]["image"], currency_with_image.image
        )

        # Clean up
        if currency_with_image.image and default_storage.exists(
            currency_with_image.image.name
        ):
            default_storage.delete(currency_with_image.image.name)

    def test_edition_detail_view_variant_sorting(self):
        """
        Test that edition_detail view properly sorts platforms and editions
        """
        base_game = Product.objects.create(
            name="Sort Test Game",
            slug="sort-test-game",
            description="Game for testing sorting",
            price=Decimal("39.99"),
            product_type=Product.BASE_GAME,
            is_active=True,
        )

        # Create variants in random order
        DigitalVariant.objects.create(
            product=base_game,
            platform=DigitalProduct.XBOX,
            edition=DigitalProduct.ULTIMATE,
            sort_order=3,
        )

        DigitalVariant.objects.create(
            product=base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.PREMIUM,
            sort_order=1,
        )

        DigitalVariant.objects.create(
            product=base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD,
            sort_order=2,
        )

        response = self.client.get(
            reverse(
                "catalog:edition_detail",
                kwargs={"product_slug": "sort-test-game"},
            )
        )

        self.assertEqual(response.status_code, 200)

        # Check that editions appear in the correct order
        editions = response.context["editions"]
        self.assertEqual(editions, ["standard", "premium", "ultimate"])

        # Check that platforms appear in variant order
        platforms = response.context["platforms"]
        self.assertEqual(platforms[0], "pc")  # First variant platform

    def test_search_with_whitespace(self):
        """Test search_results view handles whitespace correctly"""
        Product.objects.create(
            name="Test Product",
            slug="test-product",
            description="Test description",
            price=Decimal("9.99"),
            product_type=Product.DIGITAL,
            is_active=True,
        )

        # Test with leading/trailing whitespace
        response = self.client.get(
            reverse("catalog:search_results") + "?q=  Test  "
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["query"], "Test")  # Stripped


class ModelConstraintTests(TestCase):
    """Tests for model validation and database constraints"""

    def test_product_sku_uniqueness(self):
        """
        INTEGRATION TEST: Product SKU uniqueness

        Tests that the SKU generated for each product is unique across all
        products.
        """
        product1 = Product.objects.create(
            name="Game A",
            slug="game-a",
            description="First game",
            price=Decimal("29.99"),
            product_type=Product.BASE_GAME,
        )

        product2 = Product.objects.create(
            name="Game B",
            slug="game-b",
            description="Second game",
            price=Decimal("39.99"),
            product_type=Product.BASE_GAME,
        )

        # Force SKU collision
        product2.sku = product1.sku
        with self.assertRaises(IntegrityError):
            product2.save()

    def test_wishlist_with_variant(self):
        """
        INTEGRATION TEST: Wishlist item with variant

        Tests that a wishlist item can be created for a product variant,
        and that the variant is correctly linked in the wishlist.
        """
        user = User.objects.create_user(
            username="user1", email="user1@example.com", password="password123"
        )

        product = Product.objects.create(
            name="Game with Variant",
            slug="game-with-variant",
            description="Game that has variants",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
        )

        variant = DigitalVariant.objects.create(
            product=product,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD,
        )

        # Wishlist entry for the variant
        wishlist_item = Wishlist.objects.create(
            user=user, product=product, variant=variant
        )

        self.assertEqual(wishlist_item.user, user)
        self.assertEqual(wishlist_item.product, product)
        self.assertEqual(wishlist_item.variant, variant)
        self.assertIsNotNone(wishlist_item.added_at)


class SearchEdgeCaseTests(TestCase):
    """Additional edge case tests for search functionality"""

    def setUp(self):
        """Set up test data for search edge cases"""
        self.client = Client()
        # Create products for testing
        Product.objects.create(
            name="Special & Unique",
            slug="special-unique",
            description="Product with special characters in name",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            is_active=True,
        )

        Product.objects.create(
            name="Regular Product",
            slug="regular-product",
            description="A regular product without specials",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            is_active=True,
        )

    def test_search_empty_string(self):
        """Test search with empty string query"""
        response = self.client.get(reverse("catalog:search_results") + "?q=")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["query"], "")
        # No products match empty query
        self.assertEqual(response.context["total_count"], 0)

    def test_search_special_characters(self):
        """Test search with special characters in query"""
        response = self.client.get(
            reverse("catalog:search_results") + "?q=Special+%26+Unique"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_count"], 1)
        self.assertEqual(
            list(response.context["products"])[0].name, "Special & Unique"
        )


class ExtensionModelTests(TestCase):
    """Tests for product extension models edge cases"""

    def test_currency_product_zero_credits(self):
        """
        INTEGRATION TEST: Currency product with zero credits

        Tests that a CurrencyProduct can be created with zero credits,
        and that the system handles this case correctly.
        """
        product = Product.objects.create(
            name="Zero Credits",
            slug="zero-credits",
            description="Currency product with zero credits",
            price=Decimal("0.00"),
            product_type=Product.CURRENCY,
        )

        # Currency product should exist with zero credit amount
        self.assertTrue(hasattr(product, "currency"))
        self.assertEqual(product.currency.credit_amount, 0)

    def test_digital_product_platform_display(self):
        """
        INTEGRATION TEST: Digital product platform display

        Tests that the platform for a DigitalProduct is correctly set and
        displayed, especially after being saved with different casing.
        """
        product = Product.objects.create(
            name="Digital Game",
            slug="digital-game",
            description="A game available digitally",
            price=Decimal("49.99"),
            product_type=Product.DIGITAL,
        )

        # Set platform with different casing
        variant = DigitalVariant.objects.create(
            product=product,
            platform="pC",  # Mixed case
            edition=DigitalProduct.STANDARD,
        )

        # Refresh from database
        variant.refresh_from_db()
        # Platform stays as entered, no normalization
        self.assertEqual(variant.platform, "pC")

    def test_digital_product_display_with_platform_set(self):
        """Test digital product display with platform set"""
        digital = Product.objects.create(
            name="PC Game",
            slug="pc-game",
            description="Windows game",
            price=Decimal("49.99"),
            product_type=Product.DIGITAL,
        )

        # Set platform to PC
        digital.digital.platform = DigitalProduct.PC
        digital.digital.save()

        # Platform should remain as 'pc'
        self.assertEqual(digital.digital.platform, DigitalProduct.PC)  # 'pc'

        # Test string representation
        expected_str = f"{digital.name} - PC (Steam/Epic) Standard"
        self.assertEqual(str(digital.digital), expected_str)


class ViewContextTests(TestCase):
    """Tests for view context completeness and template data"""

    def setUp(self):
        """Set up test data for view context tests"""
        self.client = Client()

        # Create a base game product
        self.base_game = Product.objects.create(
            name="Base Game",
            slug="base-game",
            description="The essential base game",
            price=Decimal("49.99"),
            product_type=Product.BASE_GAME,
            is_active=True,
        )

        # Create digital variant for the base game
        self.variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD,
        )

    def test_edition_detail_context_completeness(self):
        """Test that edition_detail view provides complete context"""
        response = self.client.get(
            reverse(
                "catalog:edition_detail", kwargs={"product_slug": "base-game"}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("base_product", response.context)
        self.assertIn("selected_variant", response.context)
        self.assertIn("variants", response.context)
        self.assertIn("variants_by_platform", response.context)
        self.assertIn("platforms", response.context)
        self.assertIn("editions", response.context)

    def test_currency_detail_first_product_image_fallback(self):
        """Test currency_detail view falls back to first product image"""
        from django.core.files.uploadedfile import SimpleUploadedFile

        # Create first currency product with an image (will be first by price)
        image_file = SimpleUploadedFile(
            "test.jpg", b"fake-content", content_type="image/jpeg"
        )
        currency_with_image = Product.objects.create(
            name="100 Credits",
            slug="100-credits-with-image",
            description="Small credit pack with image",
            price=Decimal("4.99"),
            product_type=Product.CURRENCY,
            is_active=True,
            image=image_file,
        )

        # Create second currency product without image
        Product.objects.create(
            name="500 Credits",
            slug="500-credits-no-image",
            description="Large credit pack without image",
            price=Decimal("19.99"),
            product_type=Product.CURRENCY,
            is_active=True,
        )

        response = self.client.get(reverse("catalog:currency_detail"))

        self.assertEqual(response.status_code, 200)
        # Should use the first currency product's image (ordered by price)
        self.assertEqual(
            response.context["page_info"]["image"], currency_with_image.image
        )
