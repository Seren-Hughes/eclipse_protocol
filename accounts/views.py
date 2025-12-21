from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.core.paginator import Paginator
from catalog.models import Wishlist, Product, DigitalVariant
from checkout.models import Order, LicenseKey
from .forms import CustomUserCreationForm, CustomAuthenticationForm, AddressForm
from .models import Address

# Create your views here.

@login_required
def order_history(request):
    """
    Display user's order history with license keys.
    """
    orders = Order.objects.filter(user=request.user).prefetch_related(
        'items__product', 
        'items__variant',
        'items__license_keys__variant'
    ).order_by('-order_date')
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'orders': page_obj.object_list,
    }
    return render(request, 'accounts/order_history.html', context)

@login_required
def order_detail(request, order_number):
    """
    Display details for a specific order.
    """
    order = get_object_or_404(
        Order.objects.prefetch_related('items__product', 'items__variant', 'items__license_keys'),
        order_number=order_number,
        user=request.user
    )
    context = {
        'order': order,
        'items_with_keys': [
            {
                'item': item,
                'license_keys': item.license_keys.all()
            }
            for item in order.items.all()
        ]
    }
    return render(request, 'accounts/order_detail.html', context)

# --- Address Management ---

@login_required
def saved_addresses(request):
    """
    List user's saved addresses.
    """
    addresses = Address.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'addresses': addresses,
        'address_count': addresses.count(),
    }
    return render(request, 'accounts/saved_addresses.html', context)

@login_required
def add_address(request):
    """
    Add a new address.
    """
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, 'Address saved successfully!')
            return redirect('accounts:saved_addresses')
    else:
        form = AddressForm()
    context = {
        'form': form,
        'page_title': 'Add New Address',
    }
    return render(request, 'accounts/address_form.html', context)

@login_required
def edit_address(request, address_id):
    """
    Edit an existing address.
    """
    address = get_object_or_404(Address, id=address_id, user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Address updated successfully!')
            return redirect('accounts:saved_addresses')
    else:
        form = AddressForm(instance=address)
    context = {
        'form': form,
        'address': address,
        'page_title': 'Edit Address',
    }
    return render(request, 'accounts/address_form.html', context)

@login_required
@require_POST
def delete_address(request, address_id):
    """
    Delete a saved address (AJAX).
    """
    address = get_object_or_404(Address, id=address_id, user=request.user)
    try:
        address.delete()
        return JsonResponse({'success': True, 'message': 'Address deleted successfully!'})
    except Exception:
        return JsonResponse({'success': False, 'message': 'Error deleting address. Please try again.'})

# --- Authentication ---

def user_login(request):
    """Handle user login with success message and smart redirects."""
    # Get the next parameter for redirect after login
    next_url = request.GET.get('next')
    
    # Redirect if user is already logged in
    if request.user.is_authenticated:
        redirect_url = next_url if next_url else 'home'
        messages.info(request, 'You are already logged in!')
        return redirect(redirect_url)
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Use authenticate to trigger our custom backend
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                
                # go to next parameter or home
                redirect_url = next_url if next_url else 'home'
                return redirect(redirect_url)
            else:
                messages.error(request, 'Invalid username/email or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def signup(request):
    """
    User registration with redirect and messages.
    """
    next_url = request.GET.get('next')
    if request.user.is_authenticated:
        redirect_url = next_url if next_url else 'home'
        messages.info(request, 'You already have an account!')
        return redirect(redirect_url)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='accounts.backends.EmailOrUsernameBackend')
            messages.success(request, f'Welcome to Eclipse Protocol, {user.username}!')
            redirect_url = next_url if next_url else 'home'
            return redirect(redirect_url)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_logout(request):
    """
    Log out the user with a confirmation message.
    """
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.success(request, f'You have been successfully logged out. See you next time, {username}!')
    return redirect('home')

# --- Wishlist ---

@login_required
def wishlist(request):
    """Render the user's wishlist page."""
    items = Wishlist.objects.select_related(
        'product', 
        'product__currency', 
        'variant'
    ).filter(user=request.user)
    context = {
        'wishlist_items': items,
        'item_count': items.count(),
    }
    return render(request, 'accounts/wishlist.html', context)

@login_required
@require_POST
def toggle_wishlist(request, product_id):
    """Toggle a product/variant in/out of user's wishlist via AJAX."""
    product = get_object_or_404(Product, id=product_id)
    
    # Check if a variant ID was provided
    variant_id = request.POST.get('variant_id')
    variant = None
    if variant_id:
        try:
            variant = DigitalVariant.objects.get(id=variant_id, product=product)
        except DigitalVariant.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Invalid variant specified'
            })
    
    # Check if this combination already exists
    wishlist_item = Wishlist.objects.filter(
        user=request.user,
        product=product,
        variant=variant
    ).first()
    if wishlist_item:
        # Remove from wishlist
        wishlist_item.delete()
        in_wishlist = False
        message = f'Removed {product.name}'
        if variant:
            message += f' ({variant.get_platform_display()} - {variant.get_edition_display()})'
        message += ' from wishlist'
    else:
        # Add to wishlist
        Wishlist.objects.create(
            user=request.user,
            product=product,
            variant=variant
        )
        in_wishlist = True
        message = f'Added {product.name}'
        if variant:
            message += f' ({variant.get_platform_display()} - {variant.get_edition_display()})'
        message += ' to wishlist'
    
    return JsonResponse({
        'success': True,
        'in_wishlist': in_wishlist,
        'message': message
    })

@login_required
def check_wishlist(request, product_id):
    """Check if a product/variant is in user's wishlist via AJAX."""
    product = get_object_or_404(Product, id=product_id)
    
    # Check if a variant ID was provided
    variant_id = request.GET.get('variant_id')
    variant = None
    if variant_id:
        try:
            variant = DigitalVariant.objects.get(id=variant_id, product=product)
        except DigitalVariant.DoesNotExist:
            variant = None
    in_wishlist = Wishlist.objects.filter(
        user=request.user,
        product=product,
        variant=variant
    ).exists()
    
    return JsonResponse({
        'success': True,
        'in_wishlist': in_wishlist
    })

def signup(request):
    """Handle user registration with smart redirects."""
    # Get the next parameter for redirect after signup
    next_url = request.GET.get('next')
    
    # Redirect if user is already logged in
    if request.user.is_authenticated:
        redirect_url = next_url if next_url else 'home'
        messages.info(request, 'You already have an account!')
        return redirect(redirect_url)
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Specify the backend explicitly when logging in after signup
            login(request, user, backend='accounts.backends.EmailOrUsernameBackend')
            messages.success(request, f'Welcome to Eclipse Protocol, {user.username}!')
            
            # redirect to next parameter or home
            redirect_url = next_url if next_url else 'home'
            return redirect(redirect_url)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def user_logout(request):
    """Handle user logout with confirmation message."""
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.success(request, f'You have been successfully logged out. See you next time, {username}!')
    return redirect('home')