// wishlist heart toggle functionality
document.addEventListener('DOMContentLoaded', function () {
    const wishlistToggle = document.querySelector('[data-wishlist-toggle]');

    if (wishlistToggle) {
        wishlistToggle.addEventListener('click', function (e) {
            e.preventDefault();

            const icon = this.querySelector('i.fa-heart');
            const isActive = this.classList.contains('active');

            // toggle active state
            this.classList.toggle('active');

            // toggle icon classes
            if (isActive) {
                // remove from wishlist - switch to regular heart
                icon.classList.remove('fa-solid');
                icon.classList.add('fa-regular');
                this.setAttribute('aria-pressed', 'false');
                this.setAttribute('title', 'Add standard base-game to wishlist');
                this.setAttribute('aria-label', 'Add standard base-game to wishlist');
            } else {
                // add to wishlist - switch to solid heart
                icon.classList.remove('fa-regular');
                icon.classList.add('fa-solid');
                this.setAttribute('aria-pressed', 'true');
                this.setAttribute('title', 'Remove from wishlist');
                this.setAttribute('aria-label', 'Remove from wishlist');
            }
        });
    }
});
