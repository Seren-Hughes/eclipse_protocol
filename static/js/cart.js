/**
 * Cart functionality handles add-to-cart, remove, update,
 * and wishlist integration
 * Supports both authenticated and anonymous users
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize cart functionality
    initializeCartPage();
    initializeCartButtons();
});

/**
 * Initialize cart page functionality (remove buttons, etc.)
 */
function initializeCartPage() {
    // Remove item buttons
    const removeButtons = document.querySelectorAll('.btn-remove-item');
    
    removeButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const itemId = this.dataset.itemId;
            removeCartItem(itemId);
        });
    });
}

/**
 * Initialize add-to-cart buttons across the site
 */
function initializeCartButtons() {
    // Handle add to cart buttons (edition detail page and wishlist)
    const addToCartButtons = document.querySelectorAll('.btn-add-to-cart, .btn-add-to-basket');
    addToCartButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const productId = this.dataset.productId;
            let variantId = this.dataset.variantId;
            
            // For edition detail page, get current variant selection if not provided
            if (!variantId && (window.location.pathname.includes('/products/') || window.location.pathname.includes('/catalog/'))) {
                variantId = getCurrentVariantId();
            }
            
            if (!productId) {
                console.error('No product ID found for add to cart button');
                return;
            }

            // Only redirect to cart if it's specifically the BUY NOW button on currency page
            const isBuyNow = this.id === 'buyNowBtn' || (this.classList.contains('btn-buy-now') && window.location.pathname.includes('/currency/'));
            
            // Check if this is from wishlist page (for auto-removal after add)
            const isFromWishlist = window.location.pathname.includes('/wishlist/');
            
            addToCart(productId, variantId, this, isBuyNow, isFromWishlist);
        });
    });

    // Handle buy now buttons specifically for currency detail page
    const buyNowButtons = document.querySelectorAll('#buyNowBtn');
    buyNowButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Only get selected credit pack for currency pages
            const productId = getSelectedCreditPackId();
            
            if (!productId) {
                showToast('Please select a credit pack first', 'info');
                return;
            }
            
            addToCart(productId, null, this, true); // true = redirect to cart
        });
    });
}

/**
 * Add a product to the cart via AJAX
 * @param {string} productId - Product ID
 * @param {string|null} variantId - Variant ID (optional)
 * @param {HTMLElement|null} buttonElement - Button element for UI feedback
 * @param {boolean} redirectToCart - Whether to redirect to cart after success
 * @param {boolean} isFromWishlist - Whether this is from wishlist page
 */
function addToCart(productId, variantId = null, buttonElement = null, redirectToCart = false, isFromWishlist = false) {
    // Prepare form data
    const formData = new FormData();
    formData.append('quantity', '1');
    if (variantId) {
        formData.append('variant_id', variantId);
    }

    // Show loading state if button provided
    let originalText = '';
    if (buttonElement) {
        originalText = buttonElement.innerHTML;
        buttonElement.innerHTML = '<i class="fa fa-spinner fa-spin me-2"></i>Adding...';
        buttonElement.disabled = true;
    }

    fetch(`/cart/add/${productId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (redirectToCart) {
                // For "buy now" buttons on currency page - redirect to cart
                window.location.href = '/cart/';
            } else {
                // For all other buttons - show success feedback only
                if (buttonElement) {
                    buttonElement.innerHTML = '<i class="fa fa-check me-2"></i>Added!';
                    buttonElement.classList.remove('btn-primary');
                    buttonElement.classList.add('btn-success');
                    
                    // Reset button after 2 seconds
                    setTimeout(() => {
                        buttonElement.innerHTML = originalText;
                        buttonElement.classList.remove('btn-success');
                        buttonElement.classList.add('btn-primary');
                        buttonElement.disabled = false;
                    }, 2000);
                }
                
                showToast(data.message, 'success');
                updateCartBadge(data.cart_total);
                
                // Remove from wishlist if added from wishlist page
                if (isFromWishlist && buttonElement) {
                    removeFromWishlistAfterAddToCart(productId, variantId, buttonElement);
                }
            }
        } else {
            // Check if it's a "already in cart" message and use info instead of error
            const isAlreadyInCart = data.message && data.message.toLowerCase().includes('already in');
            const toastType = isAlreadyInCart ? 'info' : 'error';
            
            handleAddToCartError(buttonElement, originalText, data.message, toastType);
        }
    })
    .catch(error => {
        console.error('Error adding to cart:', error);
        handleAddToCartError(buttonElement, originalText, 'Network error - please try again', 'error');
    });
}

/**
 * Remove an item from wishlist after successfully adding to cart
 * @param {string} productId - Product ID
 * @param {string|null} variantId - Variant ID (optional)
 * @param {HTMLElement} buttonElement - Button element for finding the card to remove
 */
function removeFromWishlistAfterAddToCart(productId, variantId, buttonElement) {
    // Prepare form data for wishlist removal
    const formData = new FormData();
    if (variantId) {
        formData.append('variant_id', variantId);
    }

    // Call wishlist toggle API to remove the item
    fetch(`/accounts/wishlist/toggle/${productId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success && !data.in_wishlist) {
            // Find the wishlist card containing this button and remove it
            const wishlistCard = buttonElement.closest('.col');
            if (wishlistCard) {
                wishlistCard.style.animation = 'fadeOut 0.3s ease-out';
                setTimeout(() => {
                    wishlistCard.remove();
                    // Update wishlist count if function exists (from wishlist.js)
                    if (typeof updateWishlistCount === 'function') {
                        updateWishlistCount();
                    }
                    
                    // Check if wishlist is now empty
                    const remainingCards = document.querySelectorAll('.wishlist-card').length;
                    if (remainingCards === 0) {
                        // Show empty wishlist message
                        const container = document.querySelector('.row');
                        if (container) {
                            container.innerHTML = `
                                <div class="alert alert-info mt-4">
                                    Your wishlist is empty.
                                </div>
                            `;
                        }
                    }
                }, 300);
            }
        }
    })
    .catch(error => {
        console.error('Error removing from wishlist:', error);
        // Don't show error to user as the main action (add to cart) succeeded
    });
}

/**
 * Handle add-to-cart error states with UI feedback
 * @param {HTMLElement|null} buttonElement - Button element for UI feedback
 * @param {string} originalText - Original button text to restore
 * @param {string} message - Error message to display
 * @param {string} toastType - Type of toast notification ('error', 'warning', etc.)
 */
function handleAddToCartError(buttonElement, originalText, message, toastType = 'error') {
    if (buttonElement) {
        const isWarning = toastType === 'warning';
        const iconClass = isWarning ? 'fa-info-circle' : 'fa-exclamation-triangle';
        const buttonClass = isWarning ? 'btn-warning' : 'btn-danger';
        const buttonText = isWarning ? 'Already Added' : 'Error';
        
        buttonElement.innerHTML = `<i class="fa ${iconClass} me-2"></i>${buttonText}`;
        buttonElement.classList.remove('btn-primary');
        buttonElement.classList.add(buttonClass);
        
        setTimeout(() => {
            buttonElement.innerHTML = originalText;
            buttonElement.classList.remove(buttonClass);
            buttonElement.classList.add('btn-primary');
            buttonElement.disabled = false;
        }, 2000);
    }
    
    showToast(message || 'Failed to add to cart', toastType);
}

/**
 * Get the currently selected variant ID on edition detail pages
 * @returns {string|null} Selected variant ID or null if none selected
 */
function getCurrentVariantId() {
    const selectedPlatform = document.querySelector('.platform-btn.active')?.dataset.platform;
    const selectedEdition = document.getElementById('editionSelect')?.value;
    
    if (!selectedPlatform || !selectedEdition) return null;
    
    // Find the variant that matches current selection
    const variantData = document.querySelectorAll('#variantData [data-variant-id]');
    for (let variant of variantData) {
        if (variant.dataset.platform === selectedPlatform && 
            variant.dataset.edition === selectedEdition) {
            return variant.dataset.variantId;
        }
    }
    return null;
}

/**
 * Get the selected credit pack ID on currency detail pages
 * @returns {string|null} Selected credit pack ID or null if none selected
 */
function getSelectedCreditPackId() {
    // Only works on currency pages
    if (!window.location.pathname.includes('/currency/')) {
        return null;
    }
    
    const selectedOption = document.querySelector('.credit-option.selected');
    return selectedOption ? selectedOption.dataset.productId : null;
}

/**
 * Update the cart badge in the navigation bar
 * @param {number} itemCount - Number of items in cart
 */
function updateCartBadge(itemCount) {
    const cartBadge = document.querySelector('.cart-badge');
    if (cartBadge) {
        cartBadge.textContent = itemCount;
        cartBadge.style.display = itemCount > 0 ? 'inline' : 'none';
    }
}

/**
 * Update cart item quantity via AJAX
 * @param {string} itemId - Item ID (database ID for auth users, session key for anonymous)
 * @param {number} quantity - New quantity
 */
function updateCartItem(itemId, quantity) {
    const formData = new FormData();
    formData.append('quantity', quantity);
    
    fetch(`/cart/update/${itemId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (quantity === 0) {
                // Remove item from DOM
                document.querySelector(`[data-item-id="${itemId}"]`).remove();
            } else {
                // Update quantity display
                const quantityDisplay = document.querySelector(`[data-item-id="${itemId}"] .quantity-display`);
                quantityDisplay.textContent = quantity;
            }
            updateCartSummary(data.cart_total, data.cart_price);
        }
    })
    .catch(error => {
        console.error('Error updating cart:', error);
    });
}

/**
 * Remove an item from the cart via AJAX
 * @param {string} itemId - Item ID (database ID for auth users, session key for anonymous)
 */
function removeCartItem(itemId) {
    fetch(`/cart/remove/${itemId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.querySelector(`[data-item-id="${itemId}"]`).remove();
            updateCartSummary(data.cart_total, data.cart_price);
            
            // Reload page if cart is empty to show empty state
            if (data.cart_total === 0) {
                location.reload();
            }
        } else {
            showToast(data.message || 'Failed to remove item', 'error');
        }
    })
    .catch(error => {
        console.error('Error removing item:', error);
        showToast('Error removing item', 'error');
    });
}

/**
 * Update cart summary display with new totals
 * @param {number} itemCount - Total number of items
 * @param {number} totalPrice - Total price amount
 */
function updateCartSummary(itemCount, totalPrice) {
    // Update cart title
    const cartTitle = document.querySelector('.cart-title');
    if (cartTitle) {
        const itemText = itemCount === 1 ? 'item' : 'items';
        cartTitle.textContent = `Your shopping basket (${itemCount} ${itemText})`;
    }
    
    // Update subtotal line in summary section
    const summaryLine = document.querySelector('.summary-line span:first-child');
    if (summaryLine) {
        const itemText = itemCount === 1 ? 'item' : 'items';
        summaryLine.textContent = `Subtotal (${itemCount} ${itemText})`;
    }
    
    // Update summary prices
    const summaryPrice = document.querySelector('.summary-price');
    const totalPriceElement = document.querySelector('.total-price');
    
    if (summaryPrice) summaryPrice.textContent = `£${totalPrice.toFixed(2)}`;
    if (totalPriceElement) totalPriceElement.textContent = `£${totalPrice.toFixed(2)}`;
    
    // Update cart badge in header
    updateCartBadge(itemCount);
}

/**
 * Show a toast notification using Bootstrap toasts
 * @param {string} message - Message to display
 * @param {string} type - Toast type ('success', 'error', 'warning', 'info', etc.)
 */
function showToast(message, type = 'info') {
    // Check if Bootstrap toasts are available
    if (typeof bootstrap !== 'undefined' && bootstrap.Toast) {
        // Map toast types to Bootstrap classes and icons
        const typeConfig = {
            'success': { class: 'success', icon: 'check-circle' },
            'error': { class: 'danger', icon: 'exclamation-circle' },
            'danger': { class: 'danger', icon: 'exclamation-circle' },
            'warning': { class: 'warning', icon: 'exclamation-triangle' },
            'info': { class: 'info', icon: 'info-circle' },
            'primary': { class: 'primary', icon: 'info-circle' },
            'secondary': { class: 'secondary', icon: 'info-circle' },
            'light': { class: 'light', icon: 'info-circle' },
            'dark': { class: 'dark', icon: 'info-circle' }
        };
        
        const config = typeConfig[type] || typeConfig['info'];
        
        const toastHTML = `
            <div class="toast align-items-center text-bg-${config.class} border-0" 
                 role="alert" aria-live="assertive" aria-atomic="true" data-bs-autohide="true" data-bs-delay="4000">
                <div class="d-flex">
                    <div class="toast-body">
                        <i class="fa-solid fa-${config.icon} me-2"></i>
                        ${message}
                    </div>
                    <button type="button" class="btn-close ${config.class === 'light' ? '' : 'btn-close-white'} me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        `;
        
        let toastContainer = document.querySelector('.toast-container');
        if (!toastContainer) {
            toastContainer = document.createElement('div');
            toastContainer.className = 'toast-container position-fixed top-0 end-0 p-3';
            toastContainer.style.zIndex = '1100';
            document.body.appendChild(toastContainer);
        }
        
        toastContainer.insertAdjacentHTML('beforeend', toastHTML);
        const toastElement = toastContainer.lastElementChild;
        const toast = new bootstrap.Toast(toastElement);
        toast.show();
        
        toastElement.addEventListener('hidden.bs.toast', () => {
            toastElement.remove();
        });
    } else {
        // Fallback for environments without Bootstrap
        console.log(`${type.toUpperCase()}: ${message}`);
    }
}

/**
 * Get Django CSRF token from cookies
 * @param {string} name - Cookie name
 * @returns {string|null} Cookie value or null if not found
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Make functions globally available for other scripts
window.addToCart = addToCart;
window.showToast = showToast;