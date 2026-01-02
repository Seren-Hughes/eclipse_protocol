from decimal import Decimal

from catalog.models import DigitalVariant, Product


def cart_contents(request):
    """
    Make cart contents available across all templates.

    This context processor follows Django's standard pattern for making
    data available site-wide. Similar to how 'django.contrib.auth.context_processors.auth'
    makes {{ user }} available everywhere.

    Documentation: https://docs.djangoproject.com/en/5.2/ref/templates/api/#writing-your-own-context-processors

    Usage in templates:
        {{ cart_items }}     - List of items in cart
        {{ total }}          - Cart subtotal
        {{ product_count }}  - Total number of items
        {{ grand_total }}    - Total including delivery

    Handles both session-based and database-based carts.
    Optimized with early return for empty carts.
    """
    cart = request.session.get("cart", {})
    cart_items = []
    total = Decimal("0.00")
    product_count = 0
    delivery = Decimal("0.00")

    # Early return for empty cart - avoid unnecessary processing
    if not cart:
        return {
            "cart_items": cart_items,
            "total": total,
            "product_count": product_count,
            "delivery": delivery,
            "grand_total": total,
            "shipping_required": False,
        }

    shipping_required = False

    for item_id, item_data in cart.items():
        try:
            # Handle both simple products and variants
            if "variant_id" in item_data:
                # Base game with variant selection (PC Ultimate, Xbox Standard, etc.)
                variant = DigitalVariant.objects.get(
                    id=item_data["variant_id"]
                )
                product = variant.product
                price = variant.effective_price
                display_name = f"{product.name} - {variant.get_platform_display()} {variant.get_edition_display()}"
            else:
                # Simple product (currency packs, DLC, expansions)
                product = Product.objects.get(id=item_data["product_id"])
                variant = None
                price = product.price
                display_name = product.name

            quantity = item_data.get(
                "quantity", 1
            )  # Safer access with default
            line_total = price * quantity
            total += line_total
            product_count += quantity

            # Check if shipping required (for future physical products)
            if (
                hasattr(product, "product_type")
                and product.product_type == "PHYSICAL"
            ):
                shipping_required = True

            cart_items.append(
                {
                    "item_id": item_id,
                    "product": product,
                    "variant": variant,
                    "quantity": quantity,
                    "price": price,
                    "line_total": line_total,
                    "display_name": display_name,
                    "platform": item_data.get(
                        "platform", "PC"
                    ),  # Capture platform from cart
                }
            )

        except (Product.DoesNotExist, DigitalVariant.DoesNotExist):
            # Handle case where product/variant was deleted after being added to cart
            # Gracefully skip invalid items rather than crashing the entire site
            continue

    # Calculate delivery cost (placeholder for future physical products)
    if shipping_required:
        delivery = Decimal("3.99")  # Example: flat rate shipping

    grand_total = total + delivery

    return {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "grand_total": grand_total,
        "shipping_required": shipping_required,
    }
