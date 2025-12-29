from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import IntegrityError
from decimal import Decimal
from .models import Product, DigitalProduct, CurrencyProduct, DigitalVariant, Wishlist

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
            price=Decimal('19.99'),
            product_type=Product.BASE_GAME
        )
        self.assertTrue(base_game.sku.startswith('EP-BG-'))
        
        currency = Product.objects.create(
            name="Credits",
            slug="credits",
            description="Test credits",
            price=Decimal('9.99'),
            product_type=Product.CURRENCY
        )
        self.assertTrue(currency.sku.startswith('EP-CR-'))
    
    def test_product_string_representation(self):
        """
        UNIT TEST: Test __str__ method
        
        Simple test of string representation method - pure function behavior.
        """
        product = Product.objects.create(
            name="Eclipse Protocol",
            slug="eclipse-protocol",
            description="Test game",
            price=Decimal('29.99'),
            product_type=Product.BASE_GAME
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
            price=Decimal('24.99'),
            product_type=Product.BASE_GAME
        )
    
    def test_variant_sku_generation(self):
        """
        UNIT TEST: Test SKU generation for variants
        
        Tests the save() method logic that combines base SKU + platform + edition.
        """
        variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD
        )
        
        expected_sku = f"{self.base_game.sku}-PC-STANDARD"
        self.assertEqual(variant.sku, expected_sku)
    
    def test_effective_price_base(self):
        """
        UNIT TEST: Test effective_price property (no override)
        
        Tests @property method when price_override is None - should return base price.
        """
        variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD
        )
        
        self.assertEqual(variant.effective_price, self.base_game.price)
    
    def test_effective_price_override(self):
        """
        UNIT TEST: Test effective_price property (with override)
        
        Tests @property method when price_override is set - should return override.
        """
        variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.ULTIMATE,
            price_override=Decimal('49.99')
        )
        
        self.assertEqual(variant.effective_price, Decimal('49.99'))
    
    def test_full_description_property(self):
        """
        UNIT TEST: Test full_description property
        
        Tests the string manipulation logic that combines base + variant descriptions.
        """
        variant = DigitalVariant.objects.create(
            product=self.base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.PREMIUM,
            description="Includes season pass and exclusive skins"
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
            price=Decimal('4.99'),
            product_type=Product.CURRENCY
        )
        
        self.assertTrue(hasattr(product, 'currency'))
        self.assertEqual(product.currency.credit_amount, 0)  # Default value
    
    def test_digital_product_auto_creation(self):
        """
        INTEGRATION TEST: Signal creates DigitalProduct extension
        
        Tests integration between Product creation and DigitalProduct auto-creation.
        """
        product = Product.objects.create(
            name="DLC Pack",
            slug="dlc-pack",
            description="Extra content",
            price=Decimal('7.99'),
            product_type=Product.DIGITAL
        )
        
        self.assertTrue(hasattr(product, 'digital'))
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
            price=Decimal('39.99'),
            product_type=Product.BASE_GAME
        )
        
        with self.assertRaises(DigitalProduct.DoesNotExist):
            _ = product.digital


class WishlistIntegrationTests(TestCase):
    """Integration tests for wishlist functionality"""
    
    def setUp(self):
        """Set up User and Product for relationship testing"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.product = Product.objects.create(
            name="Wishlist Game",
            slug="wishlist-game",
            description="Game for wishlist testing",
            price=Decimal('19.99'),
            product_type=Product.BASE_GAME
        )
    
    def test_wishlist_creation(self):
        """
        INTEGRATION TEST: Wishlist model relationships
        
        Tests that Wishlist correctly links User + Product models
        and handles timestamp creation.
        """
        wishlist = Wishlist.objects.create(
            user=self.user,
            product=self.product
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
        Wishlist.objects.create(user=self.user, product=self.product, variant=None)
        
        with self.assertRaises(IntegrityError):  # IntegrityError from database
            Wishlist.objects.create(user=self.user, product=self.product, variant=None)



class DigitalVariantIntegrationTests(TestCase):
    """Integration tests for variant-product relationships"""
    
    def setUp(self):
        self.base_game = Product.objects.create(
            name="Eclipse Protocol",
            slug="eclipse-protocol", 
            description="Sci-fi strategy game",
            price=Decimal('24.99'),
            product_type=Product.BASE_GAME
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
            edition=DigitalProduct.STANDARD
        )
        
        with self.assertRaises(Exception):  # IntegrityError from database
            DigitalVariant.objects.create(
                product=self.base_game,
                platform=DigitalProduct.PC,
                edition=DigitalProduct.STANDARD
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
            username='admin',
            email='admin@example.com', 
            password='adminpass123'
        )
        self.client = Client()
        self.client.login(username='admin', password='adminpass123')
    
    def test_product_admin_accessible(self):
        """
        FUNCTIONAL TEST: Admin pages load without crashing
        
        Tests that admin views render correctly - simulates real user clicking
        through admin interface. Tests Django admin + your admin customizations.
        """
        response = self.client.get('/admin/catalog/product/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/admin/catalog/product/add/')
        self.assertEqual(response.status_code, 200)
    
    def test_variant_admin_accessible(self):
        """
        FUNCTIONAL TEST: Variant admin accessibility
        
        Ensures your custom DigitalVariant admin interface works.
        """
        response = self.client.get('/admin/catalog/digitalvariant/')
        self.assertEqual(response.status_code, 200)
    
    def test_currency_admin_accessible(self):
        """
        FUNCTIONAL TEST: Currency admin accessibility
        
        Tests that CurrencyProduct admin with custom display methods works.
        """
        response = self.client.get('/admin/catalog/currencyproduct/')
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
            price=Decimal('29.99'),
            product_type=Product.BASE_GAME
        )
        
        # Step 2: Admin adds variants for different platforms/editions
        pc_standard = DigitalVariant.objects.create(
            product=base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.STANDARD
        )
        
        pc_ultimate = DigitalVariant.objects.create(
            product=base_game,
            platform=DigitalProduct.PC,
            edition=DigitalProduct.ULTIMATE,
            price_override=Decimal('59.99'),
            description="Includes all DLC and season pass"
        )
        
        # Step 3: Verify the complete setup works correctly
        self.assertEqual(base_game.digital_variants.count(), 2)
        self.assertEqual(pc_standard.effective_price, Decimal('29.99'))  # Uses base price
        self.assertEqual(pc_ultimate.effective_price, Decimal('59.99'))  # Uses override
    
    def test_currency_workflow(self):
        """
        FUNCTIONAL TEST: Complete currency product setup
        
        Tests the workflow for creating credit packs - Product creation
        triggers signal, admin updates credit amount, system works end-to-end.
        """
        # Step 1: Admin creates currency product (signal auto-creates extension)
        currency = Product.objects.create(
            name="500 Credits",
            slug="500-credits",
            description="In-game currency",
            price=Decimal('9.99'),
            product_type=Product.CURRENCY
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
            price=Decimal('14.99'),
            product_type=Product.DIGITAL
        )
        
        # Step 2: Admin configures platform/edition details
        dlc.digital.platform = DigitalProduct.PC
        dlc.digital.edition = DigitalProduct.STANDARD
        dlc.digital.save()
        
        # Step 3: Verify complete configuration
        self.assertEqual(dlc.digital.platform, DigitalProduct.PC)
        self.assertTrue(dlc.digital.requires_key)