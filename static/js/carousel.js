// carousel functionality
document.addEventListener('DOMContentLoaded', function() {
    // Get carousel elements
    const carousel = document.querySelector('.currency-carousel');
    const prevBtn = document.querySelector('.carousel-prev');
    const nextBtn = document.querySelector('.carousel-next');
    
    // Exit if carousel elements not found
    if (!carousel || !prevBtn || !nextBtn) return;
    
    // Get all currency pack items
    const items = carousel.querySelectorAll('.currency-pack-item');
    
    // Determine items per view based on viewport width
    const itemsPerView = window.innerWidth >= 992 ? 4 : window.innerWidth >= 768 ? 2 : 1;
    const totalItems = items.length;
    
    // Calculate maximum scroll index (prevent showing empty space)
    const maxIndex = Math.max(0, totalItems - itemsPerView);
    
    // Track current scroll position
    let currentIndex = 0;
    
    /**
     * Updates carousel position and button states
     */
    function updateCarousel() {
        // disable carousel transform on mobile - cards stack vertically instead
        const isMobile = window.innerWidth <= 767;
        if (isMobile) {
            carousel.style.transform = 'none';
            return;
        }
        // Calculate offset based on item width + gap
        const itemWidth = items[0]?.offsetWidth || 0;
        const gap = 24; // 1.5rem gap (from CSS)
        const offset = currentIndex * (itemWidth + gap);
        
        // Apply transform to slide carousel
        carousel.style.transform = `translateX(-${offset}px)`;
        
        // Disable buttons at start/end positions
        prevBtn.disabled = currentIndex <= 0;
        nextBtn.disabled = currentIndex >= maxIndex;
    }
    
    /**
     * Navigate to previous card
     */
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel();
        }
    });
    
    /**
     * Navigate to next card
     */
    nextBtn.addEventListener('click', () => {
        if (currentIndex < maxIndex) {
            currentIndex++;
            updateCarousel();
        }
    });
    
    // Initialize carousel on page load
    updateCarousel();
    
    /**
     * Reset carousel on window resize to prevent layout issues
     */
    window.addEventListener('resize', () => {
        currentIndex = 0;
        updateCarousel();
    });
});