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
    const totalItems = items.length;
    
    // Track current scroll position
    let currentIndex = 0;
    
    /**
     * Get current items per view based on viewport width
     */
    function getItemsPerView() {
        return window.innerWidth >= 992 ? 4 : window.innerWidth >= 768 ? 2 : 1;
    }
    
    /**
     * Get maximum scroll index based on current viewport
     */
    function getMaxIndex() {
        const itemsPerView = getItemsPerView();
        return Math.max(0, totalItems - itemsPerView);
    }
    
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
        
        // Get current max index
        const maxIndex = getMaxIndex();
        
        // Ensure currentIndex doesn't exceed new maxIndex after resize
        if (currentIndex > maxIndex) {
            currentIndex = maxIndex;
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
        const maxIndex = getMaxIndex();
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
        // Don't reset currentIndex to 0, just recalculate limits
        updateCarousel();
    });
});