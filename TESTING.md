Contents

1. [HTML Validation](#1-html-validation)
2. [CSS Validation](#2-css-validation)
3. [JavaScript Validation](#3-javascript-validation)
4. [Python Code Quality](#4-python-code-quality)
5. [Lighthouse Performance Testing](#5-lighthouse-performance-testing)
6. [Responsiveness Design Testing](#6-responsiveness-design-testing)
7. User Story Testing
8. Automated Testing
9. Manual Testing
- Navigation Testing
- Form Testing
- Defensive Programming Testing
- Authentication Security Testing
- Input Validation
10. AWS S3 Storage Testing
11. Fixed Issues
12. Bug Reporting

## 1. HTML Validation

## HTML Validation

All pages tested using [W3C Markup Validator](https://validator.w3.org/).

| Page | URL | Status | Screenshot | Validation Link | Notes |
|------|-----|--------|------------|----------------|-------|
| [Home Store Front Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/) | `/` | ✅ | ![home validation screenshot](docs/images/test-screenshots/home-html-validation.png) | [Home Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2F) |  |
| [Login Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/login/) | `/accounts/login/` | ✅ | ![login validation screenshot](docs/images/test-screenshots/login-html-validation.png) | [Login Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Faccounts%2Flogin%2F) | See note¹ below |
| [Signup Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/signup/) | `/accounts/signup/` | ✅ | ![signup validation screenshot](docs/images/test-screenshots/signup-html-validation.png) | [Signup Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Faccounts%2Fsignup%2F) |  |
| [Order History Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/) | `/accounts/` | ✅ | ![order history validation screenshot](docs/images/test-screenshots/order-history-html-validation.png) | [Order History Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Faccounts%2F) |  |
| [Saved Addresses Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/addresses/) | `/accounts/addresses/` | ✅ | ![saved addresses validation screenshot](docs/images/test-screenshots/saved-addresses-html-validation.png) | [Saved Addresses Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Faccounts%2Faddresses%2F) |  |
| [Saved Address Form](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/addresses/add/) | `/accounts/addresses/add/` | ✅ | ![saved address form validation screenshot](docs/images/test-screenshots/saved-address-form-html-validation.png) | [Saved Address Form Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Faccounts%2Faddresses%2Fadd%2F) |  |
| [Wishlist Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/wishlist/) | `/accounts/wishlist/` | ✅ | ![wishlist validation screenshot](docs/images/test-screenshots/wishlist-html-validation.png) | Login required. Validated by text input |  |
| [Admin Sales Dashboard](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/admin/dashboard/sales/) | `/admin-dashboard/` | ✅ | ![admin sales dashboard validation screenshot](docs/images/test-screenshots/sales-dashboard-html-validation.png) | Staff login required. Validated by text input |  |
| [Search Results Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/products/search/?q=test) | `/products/search/` | ✅ | ![search results validation screenshot](docs/images/test-screenshots/search-results-html-validation.png) | [Search Results Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fproducts%2Fsearch%2F%3Fq%3Dtest) |  |
| [Currency Detail Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/products/currency/) | `/products/currency/` | ✅ | ![currency detail validation screenshot](docs/images/test-screenshots/currency-detail-html-validation.png) | [Currency Detail Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fproducts%2Fcurrency%2F) |  |
| [Game Edition Detail Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/products/base-game/eclipse-protocol/) | `/products/base-game/eclipse-protocol/` | ✅ | ![game edition detail validation screenshot](docs/images/test-screenshots/game-edition-html-validation.png) | [Game Edition Detail Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fproducts%2Fbase-game%2Feclipse-protocol%2F) |  |
| [Cart Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/cart/) | `/cart/` | ✅ | ![cart validation screenshot](docs/images/test-screenshots/cart-html-validation.png) | [Cart Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fcart%2F) |  |
| [Checkout Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/) | `/checkout/` | ✅ | ![checkout validation screenshot](docs/images/test-screenshots/checkout-html-validation.png) | Login required. Validated by text input |  |
| [Review Order Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/review/) | `/checkout/review/` | ✅ | ![review order validation screenshot](docs/images/test-screenshots/review-order-html-validation.png) | Login required. Validated by text input |  |
| [Payment Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/payment/) | `/checkout/payment/` | ✅ | ![payment page validation screenshot](docs/images/test-screenshots/payment-html-validation.png) | Login required. Validated by text input |  |
| [Order Confirmation Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/confirmation/) | `/checkout/confirmation/` | ✅ | ![order confirmation validation screenshot](docs/images/test-screenshots/order-confirmation-html-validation.png) | Login required. Validated by text input |  |
| [404 Error Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/nonexistentpage/) | `/nonexistentpage/` | ✅ | ![404 error page validation screenshot](docs/images/test-screenshots/404-html-validation.png) | Validated by text input |  |
| 500 Error Page |  | ✅ | ![500 error page validation screenshot](docs/images/test-screenshots/500-html-validation.png) | Validated by text input with temp view/url |  |
| [About Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/about/) | `/pages/about/` | ✅ | ![about page validation screenshot](docs/images/test-screenshots/about-html-validation.png) | [About Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fpages%2Fabout%2F) |  |
| [FAQs Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/faqs/) | `/pages/faqs/` | ✅ | ![faqs page validation screenshot](docs/images/test-screenshots/faqs-html-validation.png) | [FAQs Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fpages%2Ffaqs%2F) |  |
| [Contact Support Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/contact/) | `/pages/contact/` | ✅ | ![contact page validation screenshot](docs/images/test-screenshots/contact-support-html-validation.png) | [Contact Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fpages%2Fcontact%2F) |  |
| [Contact Confirmation Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/contact-confirmation/) | `/pages/contact-confirmation/` | ✅ | ![contact confirmation validation screenshot](docs/images/test-screenshots/contact-confirmation-html-validation.png) | [Contact Confirmation Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fpages%2Fcontact-confirmation%2F) |  |
| [Privacy Policy Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/privacy-policy/) | `/pages/privacy-policy/` | ✅ | ![privacy policy validation screenshot](docs/images/test-screenshots/privacy-policy-html-validation.png) | [Privacy Policy Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fpages%2Fprivacy-policy%2F) |  |
| [Terms and Conditions Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/terms-and-conditions/) | `/pages/terms-and-conditions/` | ✅ | ![terms and conditions validation screenshot](docs/images/test-screenshots/terms-and-conditions-html-validation.png) | [Terms and Conditions Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fpages%2Fterms-and-conditions%2F) |  |


**Notes:**
¹ **Login Page Language Warning:** W3C usually reports OK but occasionally flags the page as Norwegian due to automatic language detection. The page correctly uses `lang="en-GB"`, `LANGUAGE_CODE = 'en-gb'`, and `LocaleMiddleware` sends `Content-Language: en`. This intermittent issue matches a known validator [issue](https://github.com/validator/validator/issues/321). It mostly occurs on form pages with minimal text.

![login validation language warning screenshot](docs/images/test-screenshots/login-language-warning-html-validation.png)

## 2. CSS Validation

## CSS Validation

All CSS files tested using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

Files tested:
- `accounts.css`
- `admin.css`
- `base.css`
- `billing.css`
- `components.css`
- `layout.css`
- `products.css`
- `variables.css`

All CSS files passed validation. 

![css validation screenshot](docs/images/test-screenshots/css-validation.png)

## 3. JavaScript Validation

## JavaScript Validation

All JavaScript files tested using **ESLint** with configuration defined in `eslint.config.js`.

### ESLint Configuration
- Configuration file: [`eslint.config.js`](eslint.config.js)
- Environment: Browser globals with ES2024+ support
- Rules: Code quality, best practices, and consistent styling
- Special handling for Django template variables (`stripePublicKey`, `clientSecret`)
- Allows functions exposed globally for HTML event handlers

### Validation Commands
```bash

# individual file testing
eslint static/js/filename.js

# all JavaScript files testing
eslint static/js/

# individual file formatting/fixing
eslint static/js/filename.js --fix

# all JavaScript files formatting/fixing
eslint static/js/ --fix
```

### Results
No errors found. Minor warnings for intentionally unused variables that serve specific purposes:
- Functions exposed to global scope for HTML onclick handlers (`copyKey`, `addToCart`, `showToast`)
- Parameters prefixed with underscore indicating intentional non-usage (`_keyCode`)
- Functions that may be called by other scripts or event handlers (`updateCartItem`)

| File | Status | ESLint Screenshot | 
|------|--------|-------------------|
| `carousel.js` | ✅ | ![carousel eslint screenshot](docs/images/test-screenshots/eslint-carousel.png) |  
| `cart.js` | ✅ | ![cart eslint screenshot](docs/images/test-screenshots/eslint-cart.png) |  
| `currency-selection.js` | ✅ | ![currency selection eslint screenshot](docs/images/test-screenshots/eslint-currency-selection.png) |  
| `edition-selection.js` | ✅ | ![edition selection eslint screenshot](docs/images/test-screenshots/eslint-edition-selection.png) |  
| `stripe-elements.js` | ✅ | ![stripe elements eslint screenshot](docs/images/test-screenshots/eslint-stripe-elements.png) |  
| `utilities.js` | ✅ | ![utilities eslint screenshot](docs/images/test-screenshots/eslint-utilities.png) |  
| `wishlist.js` | ✅ | ![wishlist eslint screenshot](docs/images/test-screenshots/eslint-wishlist.png) |  


## 4. Python Code Quality

## Python Code Quality

All Python files tested using **Flake8** with configuration defined in `.flake8` file.

### Flake8 Configuration
- Configuration file: [`.flake8`](.flake8)
- Line length: 79 characters
- Excluded directories: migrations, __pycache__, .venv
- Key rules enforced: PEP 8 compliance, unused imports, line length, indentation

### Code Formatting
- **Black**: Automatic code formatting with 79-character line length
- **isort**: Import statement organisation and sorting
- Configuration: [`pyproject.toml`](pyproject.toml)

Commands used:
```bash
# Format all Python files
black .

# Format individual file
black path/to/file.py

# Sort imports
isort .

# Check formatting without changes
black --check .
isort --check-only .

# Run Flake8 for code quality checks
flake8 .
```

| File | Status | Flake8 Screenshot |
|------|--------|-------------------|
| `accounts` | ✅ | ![accounts flake8 screenshot](docs/images/test-screenshots/flake8-accounts.png) |  
| `cart` | ✅ | ![cart flake8 screenshot](docs/images/test-screenshots/flake8-cart.png) |  
| `catalog` | ✅ | ![catalog flake8 screenshot](docs/images/test-screenshots/flake8-catalog.png) | |  
| `checkout` | ✅ | ![checkout flake8 screenshot](docs/images/test-screenshots/flake8-checkout.png) |  
| `core` | ✅ | ![core flake8 screenshot](docs/images/test-screenshots/flake8-core.png) | 
| `eclipse_protocol` | ✅ | ![eclipse_protocol flake8 screenshot](docs/images/test-screenshots/flake8-eclipse-protocol.png) |
| `support` | ✅ | ![support flake8 screenshot](docs/images/test-screenshots/flake8-support.png) |


## 5. Lighthouse Performance Testing

## Lighthouse Performance Testing

All pages tested using Google Lighthouse for performance, accessibility, best practices, and SEO optimisation. Testing conducted on both desktop and mobile devices to ensure responsive performance. 

| Page | Desktop Results | Mobile Results | Notes |
|------|-----------------|----------------|-------|
| [Home Store Front Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/) | ![home lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-home-desktop.png) | ![home lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-home-mobile.png) |  |
| [Login Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/login/) | ![login lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-login-desktop.png) | ![login lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-login-mobile.png) |  |
| [Signup Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/signup/) | ![signup lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-signup-desktop.png) | ![signup lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-signup-mobile.png) |  |
| [Order History Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/) | ![order history lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-account-desktop.png) | ![order history lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-account-mobile.png) |  |
| [Saved Addresses Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/addresses/) | ![saved addresses lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-saved-addresses-desktop.png) | ![saved addresses lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-saved-addresses-mobile.png) |  |
| [Add/Edit Address Form](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/addresses/add/) | ![saved address form lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-save-address-form-desktop.png) | ![saved address form lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-save-address-form-mobile.png) |  |
| [Wishlist Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/wishlist/) | ![wishlist lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-wishlist-desktop.png) | ![wishlist lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-wishlist-mobile.png) |  |
| [Search Results Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/products/search/?q=test) | ![search results lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-search-desktop.png) | ![search results lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-search-mobile.png) |  |
| [Currency Detail Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/products/currency/) | ![currency detail lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-currency-detail-desktop.png) | ![currency detail lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-currency-detail-mobile.png) |  |
| [Game Edition Detail Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/products/base-game/eclipse-protocol/) | ![game edition detail lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-game-edition-desktop.png) | ![game edition detail lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-game-edition-mobile.png) |  |
| [Cart Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/cart/) | ![cart lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-cart-desktop.png) | ![cart lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-cart-mobile.png) |  |
| [Checkout Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/) | ![checkout lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-checkout-desktop.png) | ![checkout lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-checkout-mobile.png) |  |
| [Review Order Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/review/) | ![review order lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-checkout-review-desktop.png) | ![review order lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-checkout-review-mobile.png) |  |
| [Payment Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/payment/) | ![payment page lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-checkout-payment-desktop-incognito.png) | ![payment page lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-checkout-payment-mobile-incognito.png) |  |
| [Order Confirmation Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/confirmation/) | ![order confirmation lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-checkout-success-desktop.png) | ![order confirmation lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-checkout-success-mobile.png) |  |
| [404 Error Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/nonexistentpage/) | ![404 error page lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-error-desktop.png) | ![404 error page lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-error-mobile.png) |  |
| [About Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/about/) | ![about page lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-about-desktop.png) | ![about page lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-about-mobile.png) |  |
| [FAQs Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/faqs/) | ![faqs page lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-faqs-desktop.png) | ![faqs page lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-faqs-mobile.png) |  |
| [Contact Support Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/contact/) | ![contact support page lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-contact-desktop.png) | ![contact support page lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-contact-mobile.png) |  |
| [Contact Confirmation Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/contact-confirmation/) | ![contact confirmation page lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-contact-confirmation-desktop.png) | ![contact confirmation page lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-contact-confirmation-mobile.png) |  |
| [Privacy Policy Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/privacy-policy/) | ![privacy policy page lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-privacy-policy-desktop.png) | ![privacy policy page lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-privacy-policy-mobile.png) |  |
| [Terms and Conditions Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/pages/terms-and-conditions/) | ![terms and conditions page lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-terms-desktop.png) | ![terms and conditions page lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-terms-mobile.png) |  |
| [Admin Sales Dashboard](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/admin-dashboard/) | ![admin sales dashboard lighthouse desktop screenshot](docs/images/test-screenshots/lighthouse-admin-dashboard-desktop.png) | ![admin sales dashboard lighthouse mobile screenshot](docs/images/test-screenshots/lighthouse-admin-dashboard-mobile.png) | Staff login required. |


## 6. Responsiveness Design Testing
## Responsiveness Design Testing

All pages tested across various screen sizes and devices to ensure responsive design and optimal user experience. Testing conducted using browser developer tools and physical devices.

**Browsers Tested:**
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari
- Opera

**Devices Tested:**
- Desktop (various resolutions)
- Tablets
- Mobile Phones iOS and Android
- BrowserStack for cross-browser/device testing

## Home Store Front Page Responsiveness Screenshots

| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![home desktop screenshot](docs/images/responsiveness-screenshots/desktop-home-firefox.png) | ![Home tablet screenshot](docs/images/responsiveness-screenshots/tablet-home.png) | ![Home tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-home-landscape.png) | ![Home mobile screenshot](docs/images/responsiveness-screenshots/mobile-home.png) | ![Home mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-home.png) |

## Signup Page Responsiveness Screenshots

| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![signup desktop screenshot](docs/images/responsiveness-screenshots/desktop-signup-edge.png) | ![Signup tablet screenshot](docs/images/responsiveness-screenshots/tablet-signup.png) | ![Signup tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-signup.png) | ![Signup mobile screenshot](docs/images/responsiveness-screenshots/mobile-signup.png) | ![Signup mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-signup.png) |

## Login Page Responsiveness Screenshots

| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![login desktop screenshot](docs/images/responsiveness-screenshots/desktop-signin-edge.png) | ![Login tablet screenshot](docs/images/responsiveness-screenshots/tablet-signin.png) | ![Login tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-signin.png) | ![Login mobile screenshot](docs/images/responsiveness-screenshots/mobile-signin.png) | ![Login mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-signin.png) |

## Order History Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![order history desktop screenshot](docs/images/responsiveness-screenshots/desktop-order-history-chrome.png) | ![Order history tablet screenshot](docs/images/responsiveness-screenshots/tablet-order-history.png) | ![Order history tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-order-history.png) | ![Order history mobile screenshot](docs/images/responsiveness-screenshots/mobile-order-history.png) | ![Order history mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-order-history.png) |

## Saved Addresses Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![saved addresses desktop screenshot](docs/images/responsiveness-screenshots/desktop-saved-addresses-chrome.png) | ![Saved addresses tablet screenshot](docs/images/responsiveness-screenshots/tablet-saved-addresses.png) | ![Saved addresses tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-saved-addresses.png) | ![Saved addresses mobile screenshot](docs/images/responsiveness-screenshots/mobile-saved-addresses.png) | ![Saved addresses mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-saved-addresses.png) |

## Add/Edit Address Form Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![add/edit address form desktop screenshot](docs/images/responsiveness-screenshots/desktop-add-edit-saved-address-chrome.png) | ![Add/Edit address form tablet screenshot](docs/images/responsiveness-screenshots/tablet-add-edit-saved-address.png) | ![Add/Edit address form tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-add-edit-saved-address.png) | ![Add/Edit address form mobile screenshot](docs/images/responsiveness-screenshots/mobile-add-edit-address.png) | ![Add/Edit address form mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-add-edit-address.png) |

## Wishlist Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![wishlist desktop screenshot](docs/images/responsiveness-screenshots/desktop-wishlist-chrome.png) | ![Wishlist tablet screenshot](docs/images/responsiveness-screenshots/tablet-wishlist.png) | ![Wishlist tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-wishlist.png) | ![Wishlist mobile screenshot](docs/images/responsiveness-screenshots/mobile-wishlist.png) | ![Wishlist mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-wishlist.png) |

## Search Results Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![search results desktop screenshot](docs/images/responsiveness-screenshots/desktop-search-results-safari.png) | ![Search results tablet screenshot](docs/images/responsiveness-screenshots/tablet-search-results.png) | ![Search results tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-search-results.png) | ![Search results mobile screenshot](docs/images/responsiveness-screenshots/mobile-search-results.png) | ![Search results mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-search-results.png) |

## Currency Detail Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![currency detail desktop screenshot](docs/images/responsiveness-screenshots/desktop-credit-page-firefox.png) | ![Currency detail tablet screenshot](docs/images/responsiveness-screenshots/tablet-currency-detail.png) | ![Currency detail tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-currency-detail.png) | ![Currency detail mobile screenshot](docs/images/responsiveness-screenshots/mobile-currency-detail.png) | ![Currency detail mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-currency-detail.png) |

## Game Edition Detail Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![game edition detail desktop screenshot](docs/images/responsiveness-screenshots/desktop-game-editions-chrome.png) | ![Game edition detail tablet screenshot](docs/images/responsiveness-screenshots/tablet-game-edition.png) | ![Game edition detail tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-game-edition.png) | ![Game edition detail mobile screenshot](docs/images/responsiveness-screenshots/mobile-game-edition.png) | ![Game edition detail mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-game-edition.png) |

## Cart Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![cart desktop screenshot](docs/images/responsiveness-screenshots/desktop-basket-opera.png) | ![Cart tablet screenshot](docs/images/responsiveness-screenshots/tablet-cart.png) | ![Cart tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-cart.png) | ![Cart mobile screenshot](docs/images/responsiveness-screenshots/mobile-cart.png) | ![Cart mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-cart.png) |

## Checkout Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![checkout desktop screenshot](docs/images/responsiveness-screenshots/desktop-checkout-opera.png) | ![Checkout tablet screenshot](docs/images/responsiveness-screenshots/tablet-checkout.png) | ![Checkout tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-checkout.png) | ![Checkout mobile screenshot](docs/images/responsiveness-screenshots/mobile-checkout.png) | ![Checkout mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-checkout.png) |

## Review Order Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![review order desktop screenshot](docs/images/responsiveness-screenshots/desktop-checkout-review-firefox.png) | ![Review order tablet screenshot](docs/images/responsiveness-screenshots/tablet-checkout-review.png) | ![Review order tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-checkout-review.png) | ![Review order mobile screenshot](docs/images/responsiveness-screenshots/mobile-checkout-review.png) | ![Review order mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-checkout-review.png) |

## Payment Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![payment page desktop screenshot](docs/images/responsiveness-screenshots/desktop-payment-safari.png) | ![Payment page tablet screenshot](docs/images/responsiveness-screenshots/tablet-payment.png) | ![Payment page tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-payment.png) | ![Payment page mobile screenshot](docs/images/responsiveness-screenshots/mobile-payment.png) | ![Payment page mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-payment.png) |

## Order Confirmation Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![order confirmation desktop screenshot](docs/images/responsiveness-screenshots/desktop-order-success-firefox.png) | ![Order confirmation tablet screenshot](docs/images/responsiveness-screenshots/tablet-order-confirmation.png) | ![Order confirmation tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-order-confirmation.png) | ![Order confirmation mobile screenshot](docs/images/responsiveness-screenshots/mobile-order-confirmation.png) | ![Order confirmation mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-order-confirmation.png) |

## About Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![about page desktop screenshot](docs/images/responsiveness-screenshots/desktop-about-firefox.png) | ![About page tablet screenshot](docs/images/responsiveness-screenshots/tablet-about.png) | ![About page tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-about.png) | ![About page mobile screenshot](docs/images/responsiveness-screenshots/mobile-about.png) | ![About page mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-about.png) |

## FAQs Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![faqs page desktop screenshot](docs/images/responsiveness-screenshots/desktop-faq-safari.png) | ![FAQs page tablet screenshot](docs/images/responsiveness-screenshots/tablet-faqs.png) | ![FAQs page tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-faqs.png) | ![FAQs page mobile screenshot](docs/images/responsiveness-screenshots/mobile-faqs.png) | ![FAQs page mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-faqs.png) |

## Contact Support Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![contact support page desktop screenshot](docs/images/responsiveness-screenshots/desktop-contact-support-firefox.png) | ![Contact support tablet screenshot](docs/images/responsiveness-screenshots/tablet-contact-support.png) | ![Contact support tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-contact-support.png) | ![Contact support mobile screenshot](docs/images/responsiveness-screenshots/mobile-contact-support.png) | ![Contact support mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-contact-support.png) |

## Contact Confirmation Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![contact confirmation page desktop screenshot](docs/images/responsiveness-screenshots/desktop-contact-confirmation-edge.png) | ![Contact confirmation tablet screenshot](docs/images/responsiveness-screenshots/tablet-contact-confirmation.png) | ![Contact confirmation tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-contact-confirmation.png) | ![Contact confirmation mobile screenshot](docs/images/responsiveness-screenshots/mobile-contact-confirmation.png) | ![Contact confirmation mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-contact-confirmation.png) |

## Privacy Policy Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![privacy policy page desktop screenshot](docs/images/responsiveness-screenshots/desktop-privacy-policy-chrome.png) | ![Privacy policy tablet screenshot](docs/images/responsiveness-screenshots/tablet-privacy-policy.png) | ![Privacy policy tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-privacy-policy.png) | ![Privacy policy mobile screenshot](docs/images/responsiveness-screenshots/mobile-privacy-policy.png) | ![Privacy policy mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-privacy-policy.png) |

## Terms and Conditions Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape | 
|---------|--------|------------------|--------|------------------|
| ![terms and conditions page desktop screenshot](docs/images/responsiveness-screenshots/desktop-terms-chrome.png) | ![Terms and conditions tablet screenshot](docs/images/responsiveness-screenshots/tablet-terms.png) | ![Terms and conditions tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-terms.png) | ![Terms and conditions mobile screenshot](docs/images/responsiveness-screenshots/mobile-terms.png) | ![Terms and conditions mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-terms.png) |

## 404 Error Page Responsiveness Screenshots
| Desktop | Tablet | Tablet Landscape | Mobile | Mobile Landscape |
|---------|--------|------------------|--------|------------------|
| ![404 error page desktop screenshot](docs/images/responsiveness-screenshots/desktop-404-chrome.png) | ![404 error page tablet screenshot](docs/images/responsiveness-screenshots/tablet-404.png) | ![404 error page tablet landscape screenshot](docs/images/responsiveness-screenshots/tablet-landscape-404.png) | ![404 error page mobile screenshot](docs/images/responsiveness-screenshots/mobile-404.png) | ![404 error page mobile landscape screenshot](docs/images/responsiveness-screenshots/mobile-landscape-404.png) |

