document.addEventListener('DOMContentLoaded', function() {
    // set css variable for navbar height
    function setNavbarHeight() {
        const navbar = document.querySelector('.navbar-custom');
        if (navbar) {
            const navbarHeight = navbar.offsetHeight;
            document.documentElement.style.setProperty('--navbar-height', `${navbarHeight}px`);
        }
    }

    setNavbarHeight();
    window.addEventListener('resize', setNavbarHeight);

    // cache dom elements
    const platformButtons = document.querySelectorAll('.platform-btn');
    const editionSelect = document.getElementById('editionSelect');
    const addToCartBtn = document.getElementById('addToCartBtn');
    const priceDisplay = document.querySelector('.price-amount');
    
    // cache image containers
    const productImageContainer = document.querySelector('.product-image');
    const mobileProductImageContainer = document.querySelector('.mobile-product-image');
    
    // cache info containers
    const productSubtitle = document.querySelector('.product-subtitle');
    const mobileProductSubtitle = document.querySelector('.product-subtitle-mobile');
    const descriptionText = document.querySelectorAll('.description-text');
    
    // get variant data from hidden div
    const variantDataElements = document.querySelectorAll('#variantData > div');
    const variantData = Array.from(variantDataElements).map(el => ({
        id: el.dataset.variantId,
        platform: el.dataset.platform,
        edition: el.dataset.edition,
        price: el.dataset.price,
        sku: el.dataset.sku,
        imageUrl: el.dataset.imageUrl,
        platformDisplay: el.dataset.platformDisplay,
        editionDisplay: el.dataset.editionDisplay,
        description: el.dataset.description
    }));

    let selectedPlatform = document.querySelector('.platform-btn.active')?.dataset.platform;
    let selectedEdition = editionSelect?.value;

    // find matching variant based on platform and edition
    function findVariant(platform, edition) {
        return variantData.find(v => v.platform === platform && v.edition === edition);
    }

    // update ui with selected variant data
    function updateDisplay(variant) {
        if (!variant) {
            addToCartBtn.disabled = true;
            addToCartBtn.textContent = 'add to cart';
            return;
        }

        // update price
        if (priceDisplay) {
            priceDisplay.textContent = `£${variant.price}`;
        }

        // update images (desktop and mobile)
        const imgHtml = variant.imageUrl 
            ? `<img src="${variant.imageUrl}" alt="Product" class="img-fluid">`
            : '<div class="fallback-image"><i class="fa-solid fa-gamepad"></i></div>';
        
        if (productImageContainer) {
            productImageContainer.innerHTML = imgHtml;
        }
        if (mobileProductImageContainer) {
            mobileProductImageContainer.innerHTML = imgHtml;
        }

        // update platform/edition badges
        const badgeHtml = `
            <span class="platform-badge">${variant.platformDisplay}</span>
            <span class="edition-badge">${variant.editionDisplay}</span>
        `;
        if (productSubtitle) {
            productSubtitle.innerHTML = badgeHtml;
        }
        if (mobileProductSubtitle) {
            mobileProductSubtitle.innerHTML = badgeHtml;
        }

        // update description
        descriptionText.forEach(desc => {
            desc.innerHTML = variant.description.replace(/\n/g, '<br>');
        });

        // enable add to cart button
        addToCartBtn.disabled = false;
        addToCartBtn.textContent = 'add to cart';
        addToCartBtn.dataset.variantId = variant.id;
        addToCartBtn.dataset.variantSku = variant.sku;

        // update url without reload - always use base product url
        const pathParts = window.location.pathname.split('/').filter(p => p);
        // remove 'base-game' and everything after it, keep just the product slug
        const baseIndex = pathParts.indexOf('base-game');
        const productSlug = pathParts[baseIndex + 1];
        const baseUrl = `/products/base-game/${productSlug}`;
        const newUrl = `${baseUrl}/${variant.platform}/${variant.edition}/`;
        window.history.pushState({
            platform: variant.platform,
            edition: variant.edition
        }, '', newUrl);
    }

    // handle platform button clicks
    platformButtons.forEach(button => {
        button.addEventListener('click', function() {
            // remove active from all buttons
            platformButtons.forEach(btn => btn.classList.remove('active'));
            
            // add active to clicked button
            this.classList.add('active');
            
            // update selected platform
            selectedPlatform = this.dataset.platform;
            
            // find and display matching variant
            const variant = findVariant(selectedPlatform, selectedEdition);
            updateDisplay(variant);
        });
    });

    // handle edition dropdown change
    if (editionSelect) {
        editionSelect.addEventListener('change', function() {
            selectedEdition = this.value;
            
            // find and display matching variant
            const variant = findVariant(selectedPlatform, selectedEdition);
            updateDisplay(variant);
        });
    }

    // handle browser back/forward
    window.addEventListener('popstate', function(event) {
        if (event.state && event.state.platform && event.state.edition) {
            const variant = findVariant(event.state.platform, event.state.edition);
            if (variant) {
                // update button states
                platformButtons.forEach(btn => {
                    btn.classList.toggle('active', btn.dataset.platform === event.state.platform);
                });
                
                // update dropdown
                if (editionSelect) {
                    editionSelect.value = event.state.edition;
                }
                
                // update display
                selectedPlatform = event.state.platform;
                selectedEdition = event.state.edition;
                updateDisplay(variant);
            }
        }
    });

    // initialize: enable button if variant is selected
    if (selectedPlatform && selectedEdition) {
        const initialVariant = findVariant(selectedPlatform, selectedEdition);
        if (initialVariant) {
            addToCartBtn.disabled = false;
            addToCartBtn.dataset.variantId = initialVariant.id;
            addToCartBtn.dataset.variantSku = initialVariant.sku;
        }
    }
});