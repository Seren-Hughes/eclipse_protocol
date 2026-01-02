from django.db import transaction

from catalog.models import DigitalVariant, Product

from .models import Cart, CartItem


def migrate_session_cart_to_user(request, user):
    """
    Transfer session cart items to authenticated user's cart.

    Args:
        request: HTTP request with session cart data
        user: Authenticated user instance

    Returns:
        dict: Summary of migration results
    """
    session_cart = request.session.get("cart", {})

    if not session_cart:
        return {"migrated": 0, "skipped": 0, "errors": []}

    migrated_count = 0
    skipped_count = 0
    errors = []

    # Get or create user cart
    user_cart, created = Cart.objects.get_or_create(user=user)

    with transaction.atomic():
        for item_id, item_data in session_cart.items():
            try:
                # Extract product and variant info
                product_id = item_data["product_id"]
                variant_id = item_data.get("variant_id")
                quantity = item_data.get("quantity", 1)

                # Validate product exists
                product = Product.objects.get(id=product_id, is_active=True)

                # Validate variant if specified
                variant = None
                if variant_id:
                    variant = DigitalVariant.objects.get(
                        id=variant_id, product=product, is_active=True
                    )

                # Check if item already exists in user cart
                existing_item = CartItem.objects.filter(
                    cart=user_cart, product=product, variant=variant
                ).first()

                if existing_item:
                    # Merge quantities for currency products
                    if product.product_type == Product.CURRENCY:
                        existing_item.quantity += quantity
                        existing_item.save()
                        migrated_count += 1
                    else:
                        # Skip digital products already in cart
                        skipped_count += 1
                else:
                    # Create new cart item
                    CartItem.objects.create(
                        cart=user_cart,
                        product=product,
                        variant=variant,
                        quantity=quantity,
                    )
                    migrated_count += 1

            except (Product.DoesNotExist, DigitalVariant.DoesNotExist):
                errors.append(f"Product/variant not found for item {item_id}")
                continue
            except Exception as e:
                errors.append(f"Error migrating item {item_id}: {str(e)}")
                continue

    # Clear session cart after successful migration
    if "cart" in request.session:
        del request.session["cart"]
        request.session.modified = True

    return {
        "migrated": migrated_count,
        "skipped": skipped_count,
        "errors": errors,
    }
