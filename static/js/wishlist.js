// wishlist heart toggle functionality
document.addEventListener('DOMContentLoaded', function () {
    const wishlistToggle = document.querySelector('[data-wishlist-toggle]');

    if (wishlistToggle) {
        wishlistToggle.addEventListener('click', function (e) {
            e.preventDefault();

            const productId = this.dataset.productId;
            const icon = this.querySelector('i.fa-heart');
            const isActive = this.classList.contains('active');

            if (!productId) {
                console.error('No product ID found for wishlist toggle');
                return;
            }

            // Make API call to toggle wishlist
            fetch(`/accounts/wishlist/toggle/${productId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
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
                        this.setAttribute('title', 'Add standard base-game to wishlist');
                        this.setAttribute('aria-label', 'Add standard base-game to wishlist');
                    }
                    
                    console.log(data.message);
                } else {
                    console.error('Failed to toggle wishlist');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Revert any UI changes on error
            });
        });
    }

    // Handle remove buttons on wishlist page
    const removeButtons = document.querySelectorAll('.btn-remove-wishlist');
    removeButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const productId = this.dataset.productId;
            const wishlistCard = this.closest('.col');
            
            if (!productId) {
                console.error('No product ID found for remove button');
                return;
            }

            fetch(`/accounts/wishlist/toggle/${productId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
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
});

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