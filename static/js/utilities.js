document.addEventListener('DOMContentLoaded', function() {
    // Select all accordion toggle buttons on the order history page
    const accordionToggles = document.querySelectorAll('.accordion-toggle');

    accordionToggles.forEach(function(toggle) {
        // Get the selector for the collapse element this toggle controls
        const collapseSelector = toggle.getAttribute('data-bs-target');
        const collapseElement = document.querySelector(collapseSelector);

        // Skip if the collapse element is not found
        if (!collapseElement) return;

        // When the accordion section is shown, update the icon and label
        collapseElement.addEventListener('show.bs.collapse', function() {
            const icon = toggle.querySelector('i');
            const label = toggle.querySelector('.toggle-label');
            if (icon) {
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
            }
            if (label) {
                label.textContent = 'Hide Details';
            }
        });

        // When the accordion section is hidden, revert the icon and label
        collapseElement.addEventListener('hide.bs.collapse', function() {
            const icon = toggle.querySelector('i');
            const label = toggle.querySelector('.toggle-label');
            if (icon) {
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
            }
            if (label) {
                label.textContent = 'View Details';
            }
        });
    });

    // Address delete modal logic for saved addresses page
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const modalElement = document.getElementById('deleteModal');
    const confirmBtn = document.getElementById('confirmDeleteBtn');
    const addressNameElement = document.getElementById('addressName');

    if (deleteButtons.length && modalElement && confirmBtn && addressNameElement) {
        const modal = new bootstrap.Modal(modalElement);

     deleteButtons.forEach(button => {
            button.addEventListener('click', function() {
                const addressId = this.getAttribute('data-address-id');
                const addressName = this.getAttribute('data-address-name');

                addressNameElement.textContent = addressName;
                modal.show();

                confirmBtn.onclick = function() {
                    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                    fetch('/accounts/addresses/' + addressId + '/delete/', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': csrfToken
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
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
    
    // About page scroll effects
    // Select hero section elements for parallax and animation effects
    const heroTitle = document.querySelector('.about-hero-title');
    const heroSection = document.querySelector('.about-hero-section');
    const heroImage = document.querySelector('.about-hero-image');

    // Only run scroll effects if all hero elements are present
    if (heroTitle && heroSection && heroImage) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const heroHeight = heroSection.offsetHeight;
            const windowHeight = window.innerHeight;
            
            // --- Parallax Effect ---
            // Move the hero image downward as the user scrolls, revealing more of the night sky
            // parallaxSpeed controls how much slower the image moves compared to scroll
            const parallaxSpeed = 0.3; // Lower = slower movement
            const parallaxOffset = scrolled * parallaxSpeed;
            heroImage.style.setProperty('--parallax-offset', `${parallaxOffset}px`);
            
            // --- Subtle Zoom Effect ---
            // Gradually zoom the hero image as the user scrolls
            // maxScroll defines the scroll range over which zoom occurs
            const maxScroll = heroHeight * 2;
            const zoomProgress = Math.min(scrolled / maxScroll, 1); // Clamp between 0 and 1
            const startScale = 1.1; // Initial zoom
            const endScale = 1.25; // Maximum zoom
            const currentScale = startScale + (zoomProgress * (endScale - startScale));
            heroImage.style.setProperty('--zoom-scale', currentScale);
            
            // Add the parallax class to enable CSS transitions
            heroImage.classList.add('parallax');
            
            // --- Darken Image on Scroll ---
            // Add a dark overlay to the image for better text readability as user scrolls
            const darkenStart = heroHeight * 0.1; // When to start darkening
            if (scrolled > darkenStart) {
                heroImage.classList.add('darkened');
            } else {
                heroImage.classList.remove('darkened');
            }
            
            // --- Fade Out Title ---
            // Fade and move the hero title out as the user scrolls
            // fadeStart and fadeEnd define the scroll range for the fade effect
            const fadeStart = heroHeight * 0.1;
            const fadeEnd = heroHeight * 0.1; // Immediate fade (can adjust for smoother effect)
            
            if (scrolled <= fadeStart) {
                // Title fully visible
                heroTitle.style.opacity = '1';
                heroTitle.style.transform = 'translate(-50%, -50%)';
            } else if (scrolled >= fadeEnd) {
                // Title fully faded and moved up
                heroTitle.style.opacity = '0';
                heroTitle.style.transform = 'translate(-50%, -40%)';
            } else {
                // Title partially faded and moved
                const fadeProgress = (scrolled - fadeStart) / (fadeEnd - fadeStart);
                const opacity = 1 - fadeProgress;
                const translateY = -50 - (fadeProgress * 10);
                
                heroTitle.style.opacity = opacity;
                heroTitle.style.transform = `translate(-50%, ${translateY}%)`;
            }
        });
    }
});