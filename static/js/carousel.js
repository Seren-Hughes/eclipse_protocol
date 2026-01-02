// carousel functionality
document.addEventListener('DOMContentLoaded', function() {
    // Get carousel elements
    const carousel = document.getElementById('currency-carousel') || document.querySelector('.currency-carousel');
    const prevBtn = document.querySelector('.carousel-btn.carousel-prev');
    const nextBtn = document.querySelector('.carousel-btn.carousel-next');

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
     * Get gap size between items
     */
    function getGap() {
        if (!items[0]) return 24;
        const style = window.getComputedStyle(items[0]);
        // Try common properties, fall back to 24px
        const gapVal = style.marginRight || style.gap || style.columnGap;
        const parsed = parseFloat(gapVal);
        return Number.isFinite(parsed) ? parsed : 24;
    }

    /**
     * Updates carousel position and button states
     */
    function updateCarousel() {
        // disable carousel transform on mobile - cards stack vertically instead
        const isMobile = window.innerWidth <= 767;
        if (isMobile) {
            carousel.style.transform = 'none';
            prevBtn.disabled = true;
            nextBtn.disabled = true;
            return;
        }

        // Get current max index
        const maxIndex = getMaxIndex();

        // Ensure currentIndex doesn't exceed new maxIndex after resize
        if (currentIndex > maxIndex) {
            currentIndex = maxIndex;
        }

        // Handle case with no items
        if (items.length === 0) {
            carousel.style.transform = 'none';
            prevBtn.disabled = true;
            nextBtn.disabled = true;
            return;
        }

        // Calculate offset based on item width + gap
        const itemWidth = items[0].offsetWidth || 0;
        const gap = getGap();
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
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(updateCarousel, 120);
    });
    window.addEventListener('orientationchange', () => setTimeout(updateCarousel, 120));
});