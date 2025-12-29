/**
 * Functions included:
 * - License key copy functionality with Clipboard API
 * - Order history accordion interactions
 * - Address management modal handlers  
 * - About page scroll effects 
 */

/**
 * Copy license key to clipboard with visual feedback
 * 
 * Uses Clipboard API when available in secure contexts (HTTPS).
 * Provides graceful fallback for non-secure contexts by selecting text
 * for manual copying. 
 * 
 * @param {string} keyCode - The license key string to copy
 * @param {HTMLElement} buttonElement - The copy button clicked by user
 */
function copyKey(keyCode, buttonElement) {
    // Check if Clipboard API is available (requires secure context)
    if (navigator.clipboard && window.isSecureContext) {
        // Use Clipboard API for automatic copying
        navigator.clipboard.writeText(keyCode).then(function() {
            showCopySuccess(buttonElement);
        }).catch(function(err) {
            console.error('Failed to copy: ', err);
            // Fall back to manual selection if clipboard fails
            showCopyFallback(buttonElement, keyCode);
        });
    } else {
        // For non-secure contexts or older browsers, enable manual copy
        showCopyFallback(buttonElement, keyCode);
    }
}

/**
 * Display success feedback when license key is copied successfully
 * 
 * Changes button appearance with checkmark icon for 1 second,
 * then reverts to original state.
 * 
 * @param {HTMLElement} buttonElement - The copy button to update
 */
function showCopySuccess(buttonElement) {
    const originalIcon = buttonElement.querySelector('i');
    const originalClass = originalIcon.className;
    
    // Change to success state: green background with checkmark
    originalIcon.className = 'fa-solid fa-check';
    buttonElement.classList.add('btn-success');
    buttonElement.classList.remove('btn-secondary');
    
    // Revert to original state after 1 second
    setTimeout(function() {
        originalIcon.className = originalClass;
        buttonElement.classList.remove('btn-success');
        buttonElement.classList.add('btn-secondary');
    }, 1000);
}

/**
 * Handle fallback copy method when Clipboard API is unavailable
 * 
 * Selects the text in the license key input field and shows visual
 * feedback to guide user to manually copy with Ctrl+C.
 * 
 * @param {HTMLElement} buttonElement - The copy button to update  
 * @param {string} keyCode - The license key (currently unused in fallback)
 */
function showCopyFallback(buttonElement, keyCode) {
    // Find the license key input field next to the button
    const keyInput = buttonElement.parentElement.querySelector('.key-code');
    if (keyInput) {
        // Select all text in the input field
        keyInput.select();
        keyInput.setSelectionRange(0, 99999); // For mobile device compatibility
        
        // Show visual feedback that text is selected for manual copy
        const originalIcon = buttonElement.querySelector('i');
        const originalClass = originalIcon.className;
        
        // Change to warning state: orange background with pointer icon
        originalIcon.className = 'fa-solid fa-hand-pointer';
        buttonElement.classList.add('btn-warning');
        buttonElement.classList.remove('btn-secondary');
        buttonElement.title = 'Text selected - press Ctrl+C to copy';
        
        // Revert to original state after 3 seconds
        setTimeout(function() {
            originalIcon.className = originalClass;
            buttonElement.classList.remove('btn-warning');
            buttonElement.classList.add('btn-secondary');
            buttonElement.title = 'Copy license key';
        }, 3000);
    } else {
        // If input field not found, show error state
        showCopyError(buttonElement);
    }
}

/**
 * Display error feedback when copy operation fails
 * 
 * Changes button appearance to red with X icon for 2 seconds,
 * then reverts to original state.
 * 
 * @param {HTMLElement} buttonElement - The copy button to update
 */
function showCopyError(buttonElement) {
    const originalIcon = buttonElement.querySelector('i');
    const originalClass = originalIcon.className;
    
    // Change to error state: red background with X icon
    originalIcon.className = 'fa-solid fa-times';
    buttonElement.classList.add('btn-danger');
    buttonElement.classList.remove('btn-secondary');
    
    // Revert to original state after 1 second
    setTimeout(function() {
        originalIcon.className = originalClass;
        buttonElement.classList.remove('btn-danger');
        buttonElement.classList.add('btn-secondary');
    }, 1000);
}

/**
 * Initialize DOM-dependent functionality when page loads
 * 
 * Sets up event handlers for:
 * - Order history accordion toggles
 * - Address management modals
 * - About page scroll effects
 */
document.addEventListener('DOMContentLoaded', function() {
    
    /**
     * Order History Accordion Management
     * 
     * Handles the expand/collapse functionality for order details.
     * Updates button icons and labels based on accordion state.
     */
    const accordionToggles = document.querySelectorAll('.accordion-toggle');

    accordionToggles.forEach(function(toggle) {
        // Get the collapse element this button controls
        const collapseSelector = toggle.getAttribute('data-bs-target');
        const collapseElement = document.querySelector(collapseSelector);

        // Skip if the collapse element is not found
        if (!collapseElement) return;

        // Update UI when accordion section is expanded
        collapseElement.addEventListener('show.bs.collapse', function() {
            const icon = toggle.querySelector('i');
            const label = toggle.querySelector('.toggle-label');
            
            // Change chevron from down to up
            if (icon) {
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
            }
            
            // Change label from "View Details" to "Hide Details"
            if (label) {
                label.textContent = 'Hide Details';
            }
        });

        // Update UI when accordion section is collapsed
        collapseElement.addEventListener('hide.bs.collapse', function() {
            const icon = toggle.querySelector('i');
            const label = toggle.querySelector('.toggle-label');
            
            // Change chevron from up to down
            if (icon) {
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
            }
            
            // Change label from "Hide Details" to "View Details"
            if (label) {
                label.textContent = 'View Details';
            }
        });
    });

    /**
     * Address Management Modal Logic
     * 
     * Handles delete confirmation modals for saved billing addresses.
     * Sends AJAX requests to delete addresses without page reload.
     */
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const modalElement = document.getElementById('deleteModal');
    const confirmBtn = document.getElementById('confirmDeleteBtn');
    const addressNameElement = document.getElementById('addressName');

    // Only set up modal logic if all required elements exist
    if (deleteButtons.length && modalElement && confirmBtn && addressNameElement) {
        const modal = new bootstrap.Modal(modalElement);

        deleteButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Get address details from button data attributes
                const addressId = this.getAttribute('data-address-id');
                const addressName = this.getAttribute('data-address-name');

                // Update modal content with address name
                addressNameElement.textContent = addressName;
                modal.show();

                // Handle confirmation click
                confirmBtn.onclick = function() {
                    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                    // Send DELETE request to server
                    fetch('/accounts/addresses/' + addressId + '/delete/', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': csrfToken
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            // Reload page to show updated address list
                            location.reload();
                        } else {
                            alert('Error: ' + data.message);
                        }
                        modal.hide();
                    })   
                    .catch(error => {
                        console.error('Error:', error);
                        alert('Error deleting address. Please try again.');
                        modal.hide();
                    });
                };
            });
        });
    }
    
    /**
     * About Page Scroll Effects
     * 
     * Creates parallax scrolling and fade effects for the hero section.
     * Includes parallax image movement, subtle zoom, darkening overlay,
     * and title fade-out as user scrolls.
     */
    const heroTitle = document.querySelector('.about-hero-title');
    const heroSection = document.querySelector('.about-hero-section');
    const heroImage = document.querySelector('.about-hero-image');

    // Only enable scroll effects if all hero elements are present
    if (heroTitle && heroSection && heroImage) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const heroHeight = heroSection.offsetHeight;
            
            /**
             * Parallax Effect
             * Moves hero image downward slower than scroll speed to create depth.
             * Lower parallaxSpeed values create more subtle movement.
             */
            const parallaxSpeed = 0.3; // 30% of scroll speed
            const parallaxOffset = scrolled * parallaxSpeed;
            heroImage.style.setProperty('--parallax-offset', `${parallaxOffset}px`);
            
            /**
             * Subtle Zoom Effect
             * Gradually scales the hero image as user scrolls.
             */
            const maxScroll = heroHeight * 2;
            const zoomProgress = Math.min(scrolled / maxScroll, 1); // Clamp 0-1
            const startScale = 1.1; // Initial 110% zoom
            const endScale = 1.25; // Maximum 125% zoom
            const currentScale = startScale + (zoomProgress * (endScale - startScale));
            heroImage.style.setProperty('--zoom-scale', currentScale);
            
            // Enable CSS transitions for smooth animation
            heroImage.classList.add('parallax');
            
            /**
             * Darken Image on Scroll
             * Adds dark overlay for better text readability.
             * Only starts darkening after initial scroll threshold.
             */
            const darkenStart = heroHeight * 0.1; // Start at 10% of hero height
            if (scrolled > darkenStart) {
                heroImage.classList.add('darkened');
            } else {
                heroImage.classList.remove('darkened');
            }
            
            /**
             * Fade Out Title
             * Gradually fades and moves title upward as user scrolls.
             * Creates professional transition effect.
             */
            const fadeStart = heroHeight * 0.1;
            const fadeEnd = heroHeight * 0.1; // Immediate fade (can be adjusted)
            
            if (scrolled <= fadeStart) {
                // Title fully visible at original position
                heroTitle.style.opacity = '1';
                heroTitle.style.transform = 'translate(-50%, -50%)';
            } else if (scrolled >= fadeEnd) {
                // Title fully faded and moved up
                heroTitle.style.opacity = '0';
                heroTitle.style.transform = 'translate(-50%, -40%)';
            } else {
                // Title transitioning (partially faded and moved)
                const fadeProgress = (scrolled - fadeStart) / (fadeEnd - fadeStart);
                const opacity = 1 - fadeProgress;
                const translateY = -50 - (fadeProgress * 10); // Move up 10% during fade
                
                heroTitle.style.opacity = opacity;
                heroTitle.style.transform = `translate(-50%, ${translateY}%)`;
            }
        });
    }
});