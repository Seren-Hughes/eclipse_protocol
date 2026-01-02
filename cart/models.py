from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models

from catalog.models import DigitalVariant, Product


class Cart(models.Model):
    """
    Persistent cart for logged-in users.

    Follows the hybrid pattern where:
    - Anonymous users: cart data stored in session
    - Logged-in users: cart data can be synced to database for persistence

    This allows users to maintain their cart across browser sessions
    and provides data for customer support and analytics.

    Related name 'cart' allows: user.cart.total_items
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    @property
    def total_items(self):
        """Total quantity of all items in cart"""
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self):
        """Total price of all items in cart (excluding delivery)"""
        return sum(item.line_total for item in self.items.all())


class CartItem(models.Model):
    """
    Individual items in a cart.

    Supports the flexible product system:
    - Simple products (currency, DLC): product field only
    - Base game variants: product + variant fields

    The unique_together constraint prevents duplicate items and handles
    the case where same product can have multiple variants.

    Examples:
    - CartItem(product=currency_pack, variant=None)
    - CartItem(product=base_game, variant=pc_ultimate_edition)
    - CartItem(product=base_game, variant=xbox_standard_edition)
    """

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(
        DigitalVariant, on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [
            "cart",
            "product",
            "variant",
        ]  # Prevent duplicate cart items

    def __str__(self):
        if self.variant:
            return f"{self.product.name} - {self.variant} x{self.quantity}"
        return f"{self.product.name} x{self.quantity}"

    @property
    def effective_price(self):
        """
        Get price from variant if available, otherwise from base product.

        This handles the pricing hierarchy:
        1. Variant price override (if variant exists and has override)
        2. Base product price (fallback for variants + only option for simple products)
        """
        if self.variant:
            return self.variant.effective_price
        return self.product.price

    @property
    def line_total(self):
        """Total price for this cart item (price x quantity)"""
        return self.effective_price * self.quantity
