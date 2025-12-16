// wishlist heart toggle functionality
document.addEventListener('DOMContentLoaded', function () {
    // Get ALL wishlist toggle buttons
    const wishlistToggles = document.querySelectorAll('[data-wishlist-toggle]');

    // Load initial wishlist state for all buttons
    loadWishlistState();

    wishlistToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function (e) {  
            e.preventDefault();

            const productId = this.dataset.productId;
            const variantId = this.dataset.variantId || getCurrentVariantId(); // For edition pages
            const icon = this.querySelector('i.fa-heart');

            if (!productId) {
                console.error('No product ID found for wishlist toggle');
                return;
            }

            // Prepare form data
            const formData = new FormData();
            if (variantId) {
                formData.append('variant_id', variantId);
            }

            // Make API call to toggle wishlist
            fetch(`/accounts/wishlist/toggle/${productId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Update UI based on server response
                    if (data.in_wishlist) {
                        // Added to wishlist - switch to solid heart
                        this.classList.add('active');
                        icon.classList.remove('fa-regular');
                        icon.classList.add('fa-solid');
                        this.setAttribute('aria-pressed', 'true');
                        this.setAttribute('title', 'Remove from wishlist');
                        this.setAttribute('aria-label', 'Remove from wishlist');
                    } else {
                        // Removed from wishlist - switch to regular heart
                        this.classList.remove('active');
                        icon.classList.remove('fa-solid');
                        icon.classList.add('fa-regular');
                        this.setAttribute('aria-pressed', 'false');
                        this.setAttribute('title', 'Add to wishlist');
                        this.setAttribute('aria-label', 'Add to wishlist');
                    }
                    
                    console.log(data.message);
                } else {
                    console.error('Failed to toggle wishlist:', data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    // Handle remove buttons on wishlist page
    const removeButtons = document.querySelectorAll('.btn-remove-wishlist');
    removeButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const productId = this.dataset.productId;
            const variantId = this.dataset.variantId;
            const wishlistCard = this.closest('.col');
            
            if (!productId) {
                console.error('No product ID found for remove button');
                return;
            }

            // Prepare form data
            const formData = new FormData();
            if (variantId) {
                formData.append('variant_id', variantId);
            }

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
                    // Remove the card from the page
                    wishlistCard.style.animation = 'fadeOut 0.3s ease-out';
                    setTimeout(() => {
                        wishlistCard.remove();
                        updateWishlistCount();
                    }, 300);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    // Listen for platform/edition changes on edition detail pages
    const platformBtns = document.querySelectorAll('.platform-btn');
    const editionSelect = document.getElementById('editionSelect');

    if (platformBtns.length > 0 || editionSelect) {
        // When platform or edition changes, update wishlist button state
        platformBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                setTimeout(loadWishlistState, 100); // Small delay to let variant data update
            });
        });

        if (editionSelect) {
            editionSelect.addEventListener('change', function() {
                setTimeout(loadWishlistState, 100);
            });
        }
    }
});

// Get current variant ID from the edition detail page
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

// Load initial wishlist state for all buttons when page loads
function loadWishlistState() {
    const wishlistToggles = document.querySelectorAll('[data-wishlist-toggle]');
    
    wishlistToggles.forEach(function(toggle) {
        const productId = toggle.dataset.productId;
        const variantId = toggle.dataset.variantId || getCurrentVariantId();
        
        if (!productId) return;
        
        // Build query string
        let url = `/accounts/wishlist/check/${productId}/`;
        if (variantId) {
            url += `?variant_id=${variantId}`;
        }
        
        // Check if this product/variant is in the user's wishlist
        fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const icon = toggle.querySelector('i.fa-heart');
                
                if (data.in_wishlist) {
                    // Product is in wishlist - show solid heart
                    toggle.classList.add('active');
                    icon.classList.remove('fa-regular');
                    icon.classList.add('fa-solid');
                    toggle.setAttribute('aria-pressed', 'true');
                    toggle.setAttribute('title', 'Remove from wishlist');
                    toggle.setAttribute('aria-label', 'Remove from wishlist');
                } else {
                    // Product not in wishlist - show regular heart
                    toggle.classList.remove('active');
                    icon.classList.remove('fa-solid');
                    icon.classList.add('fa-regular');
                    toggle.setAttribute('aria-pressed', 'false');
                    toggle.setAttribute('title', 'Add to wishlist');
                    toggle.setAttribute('aria-label', 'Add to wishlist');
                }
            }
        })
        .catch(error => {
            console.error('Error checking wishlist state:', error);
        });
    });
}

// Helper function to get CSRF token from cookies
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

// Helper function to update wishlist count
function updateWishlistCount() {
    const wishlistItems = document.querySelectorAll('.wishlist-card').length;
    const countElement = document.querySelector('.wishlist-title');
    if (countElement) {
        const itemText = wishlistItems === 1 ? 'item' : 'items';
        countElement.textContent = `Your Wishlist (${wishlistItems} ${itemText})`;
    }
}