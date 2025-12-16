from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse
from catalog.models import Wishlist, Product
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.

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

@login_required
def wishlist(request):
    """Render the user's wishlist page."""
    items = Wishlist.objects.select_related('product', 'product__currency').filter(user=request.user)
    context = {
        'wishlist_items': items,
        'item_count': items.count(),
    }
    return render(request, 'accounts/wishlist.html', context)

@login_required
@require_POST
def toggle_wishlist(request, product_id):
    """Toggle a product in/out of user's wishlist via AJAX."""
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )
    
    if not created:
        # remove from wishlist
        wishlist_item.delete()
        in_wishlist = False
    else:
        # add to wishlist
        in_wishlist = True
    
    return JsonResponse({
        'success': True,
        'in_wishlist': in_wishlist,
        'message': 'Added to wishlist' if in_wishlist else 'Removed from wishlist'
    })

@login_required
def check_wishlist(request, product_id):
    """Check if a product is in user's wishlist via AJAX."""
    product = get_object_or_404(Product, id=product_id)
    in_wishlist = Wishlist.objects.filter(user=request.user, product=product).exists()
    
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