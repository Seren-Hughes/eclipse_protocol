document.addEventListener('DOMContentLoaded', function() {
    // set css variable for navbar height based on actual element
    // to help with sticky positioning (currency image on detail page)
    function setNavbarHeight() {
        const navbar = document.querySelector('.navbar-custom');
        if (navbar) {
            const navbarHeight = navbar.offsetHeight;
            document.documentElement.style.setProperty('--navbar-height', `${navbarHeight}px`);
        }
    }

    // run on page load and window resize
    setNavbarHeight();
    window.addEventListener('resize', setNavbarHeight);

    // cache dom elements for product selection and display
    const creditOptions = document.querySelectorAll('.credit-option');
    const buyNowBtn = document.getElementById('buyNowBtn');
    let selectedProductId = null;

    // cache elements for updating product info and image
    const productImage = document.querySelector('.product-image img');
    const fallbackImage = document.querySelector('.fallback-image');
    const productTitle = document.querySelector('.product-title');
    const productImageContainer = document.querySelector('.product-image');

    // handle credit option selection
    creditOptions.forEach(option => {
        option.addEventListener('click', function() {
            // remove previous selection
            creditOptions.forEach(opt => opt.classList.remove('selected'));
            // add selection to clicked option
            this.classList.add('selected');

            // get product data from dataset
            selectedProductId = this.dataset.productId;
            const productSlug = this.dataset.productSlug;
            const credits = this.dataset.credits;
            const price = this.dataset.price;

            // update product display on left side
            updateProductDisplay(this);

            // update url for selected product without reload
            const newUrl = `/products/currency/${productSlug}/`;
            window.history.pushState({
                productId: selectedProductId, 
                productSlug: productSlug,
                credits: credits,
                price: price
            }, '', newUrl);

            // enable buy now button and update text
            buyNowBtn.disabled = false;
            buyNowBtn.textContent = `BUY ${credits} CREDITS - £${price}`;
        });
    });

    // update product info and image based on selected option
    function updateProductDisplay(selectedOption) {
        const credits = selectedOption.dataset.credits;
        const productName = selectedOption.dataset.productName || `${credits} Eclipse Protocol Credits`;
        const imageUrl = selectedOption.dataset.imageUrl;

        // update product title
        if (productTitle) {
            productTitle.textContent = productName;
        }

        // update product image or fallback icon
        if (imageUrl && imageUrl.trim() !== '') {
            if (productImageContainer) {
                productImageContainer.innerHTML = '';
                const img = document.createElement('img');
                img.src = imageUrl;
                img.alt = productName;
                img.className = 'img-fluid';
                productImageContainer.appendChild(img);
            }
        } else {
            if (productImageContainer) {
                productImageContainer.innerHTML = '';
                const fallback = document.createElement('div');
                fallback.className = 'fallback-image';
                fallback.innerHTML = '<i class="fa-solid fa-coins"></i>';
                productImageContainer.appendChild(fallback);
            }
        }
    }

    // handle browser back/forward navigation
    window.addEventListener('popstate', function(event) {
        if (event.state && event.state.productId) {
            selectProductById(event.state.productId);
        } else {
            clearSelection();
        }
    });

    // select product on page load if url matches a product slug
    const currentPath = window.location.pathname;
    const pathMatch = currentPath.match(/\/products\/currency\/([^\/]+)\//);
    if (pathMatch) {
        const selectedSlug = pathMatch[1];
        selectProductBySlug(selectedSlug);
    }

    // select product by id helper
    function selectProductById(productId) {
        const option = document.querySelector(`[data-product-id="${productId}"]`);
        if (option) {
            option.click();
        }
    }

    // select product by slug helper
    function selectProductBySlug(slug) {
        const option = document.querySelector(`[data-product-slug="${slug}"]`);
        if (option) {
            option.click();
        }
    }

    // clear selection and reset product info
    function clearSelection() {
        creditOptions.forEach(opt => opt.classList.remove('selected'));
        if (productTitle) {
            productTitle.textContent = 'Eclipse Protocol Credits';
        }
        if (productImageContainer) {
            productImageContainer.innerHTML = '';
            const fallback = document.createElement('div');
            fallback.className = 'fallback-image';
            fallback.innerHTML = '<i class="fa-solid fa-coins"></i>';
            productImageContainer.appendChild(fallback);
        }
        buyNowBtn.disabled = true;
        buyNowBtn.textContent = 'BUY NOW';
        selectedProductId = null;
    }

    // wishlist heart toggle functionality
    const wishlistToggles = document.querySelectorAll('[data-wishlist-toggle]');
    wishlistToggles.forEach(function(wishlistToggle) {
        wishlistToggle.addEventListener('click', function (e) {
            e.preventDefault();
            const icon = this.querySelector('i.fa-heart');
            const isActive = this.classList.contains('active');
            const productId = this.dataset.productId;

            // toggle active state and icon style
            this.classList.toggle('active');
            if (isActive) {
                icon.classList.remove('fa-solid');
                icon.classList.add('fa-regular');
                this.setAttribute('aria-pressed', 'false');
                this.setAttribute('title', 'Add to wishlist');
                this.setAttribute('aria-label', 'Add to wishlist');
            } else {
                icon.classList.remove('fa-regular');
                icon.classList.add('fa-solid');
                this.setAttribute('aria-pressed', 'true');
                this.setAttribute('title', 'Remove from wishlist');
                this.setAttribute('aria-label', 'Remove from wishlist');
            }

            // TO DO:ajax call for wishlist toggle to go here
        });
    });
});