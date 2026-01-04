Contents

1. [HTML Validation](#1-html-validation)
2. [CSS Validation](#2-css-validation)
3. [JavaScript Validation](#3-javascript-validation)
4. [Python Code Quality](#4-python-code-quality)
5. [Lighthouse Performance Testing](#5-lighthouse-performance-testing)
6. [Responsiveness Design Testing](#6-responsiveness-design-testing)
7. [User Story Testing](#7-user-story-testing)
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

## 7. User Story Testing

User story testing conducted to ensure all features meet specified requirements and function as intended. Each user story tested individually with documented results according to acceptance criteria from [GitHub Project Board](https://github.com/users/Seren-Hughes/projects/9).

### Theme 1: Digital Storefront

#### Epic 1.1: Browse & Discover Digital Products

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 1.1.1 | As a customer, I want to browse all available digital products (base game, DLC, credits etc.) so I can see what's available for my platform. | 1. Navigate to home page<br>2. View product listings<br>3. Check all product types are displayed | All digital products visible with clear categorisation | ✅ Products displayed correctly by type | ✅ PASS | Site shows currency packs and game editions |
| 1.1.2 | As a customer, I want to filter digital items by platform (Steam, Xbox, Nintendo, PlayStation) so I only see compatible content. | 1. Access product filtering<br>2. Select platform filter<br>3. Verify results match platform | Only platform-compatible products shown | ⏸️ Not implemented in MVP | ⏸️ Deferred | _Should have_ priority for phase 2 development |
| 1.1.3 | As a customer, I want to sort or filter by relevance or price so I can easily find what I want. | 1. Access sorting options<br>2. Sort by price<br>3. Verify correct order | Products sorted according to selected criteria | ⏸️ Not implemented in MVP | ⏸️ Deferred | _Should have_ priority for phase 2 development |

#### Epic 1.2: Product Details

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 1.2.1 | As a customer, I want to view detailed product pages with descriptions, editions, prices, and platform options so I can make informed decisions. | 1. Click on product<br>2. Review product detail page<br>3. Check all information present | Complete product information displayed | ✅ All details shown clearly | ✅ PASS | Detailed product pages include descriptions, pricing, and platform options |
| 1.2.2 | As a customer, I want to see information on delivery method (redeemable key or automatic activation) before purchase. | 1. View product details<br>2. Check delivery method information<br>3. Verify clarity before purchase | Delivery method clearly indicated | ✅ Delivery method specified | ✅ PASS | License key delivery method clearly stated |

#### Epic 1.3: Product Management (Admin)

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 1.3.1 | As a site admin, I want to create, edit, and delete product listings so I can manage the catalogue easily. | 1. Log in as admin<br>2. Access Django admin<br>3. Create/edit/delete products<br>4. Verify changes reflect on site | Product CRUD operations work correctly | ✅ Admin management functional | ✅ PASS | Full CRUD functionality available in Django admin |

### Theme 2: Digital Checkout & Delivery

#### Epic 2.1: Purchase & Payment

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 2.1.1 | As a customer, I want to add digital items to my basket and securely purchase them so I can access them in my account. | 1. Add items to cart<br>2. Proceed to checkout<br>3. Complete payment<br>4. Check account for items | Items successfully added to cart and purchased | ✅ Cart and checkout functionality works | ✅ PASS | Full shopping cart and secure checkout implemented |
| 2.1.2 | As a customer, I want to view an order summary and confirm before paying. | 1. Add items to cart<br>2. Proceed to checkout<br>3. Review order summary<br>4. Confirm before payment | Clear order summary with confirmation step | ✅ Order review step present | ✅ PASS | Order review page implemented before payment |

#### Epic 2.2: Delivery & Key Management

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 2.2.1 | As a customer, I want my digital key or credits to be automatically applied to my account and emailed after purchase. | 1. Complete purchase<br>2. Check email for confirmation<br>3. Check account dashboard<br>4. Verify keys/credits delivered | Digital items delivered automatically with email confirmation | ✅ Automatic delivery works | ✅ PASS | License keys generated and emailed automatically |

#### Epic 2.3: Order History

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 2.3.1 | As a customer, I want to view my order history with product names, dates, and total amounts so I can track past purchases. | 1. Log into account<br>2. Navigate to order history<br>3. Review past orders<br>4. Verify details are complete | Complete order history with all relevant details | ✅ Order history page functional | ✅ PASS | Comprehensive order history in account dashboard |

#### Epic 2.4: License Management (Admin)

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 2.4.1 | As a site admin, I want to manage license key generation and mark keys as redeemed so availability stays accurate. | 1. Log in as admin<br>2. Access license key management<br>3. View key generation<br>4. Check redemption tracking | License keys managed effectively by admin | ✅ Admin license management works | ✅ PASS | License key management available in Django admin |

### Theme 3: Merchandise Store

#### Epic 3.1: Browse & Purchase Merchandise

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 3.1.1 | As a customer, I want to browse official merchandise (t-shirts, hoodies, mugs) so I can support the brand I enjoy. | 1. Navigate to merchandise section<br>2. Browse available items<br>3. View product details | Merchandise products clearly displayed | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Could Have_ priority - planned for Phase 3 |

#### Epic 3.2: Checkout & Delivery

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 3.2.1 | As a customer, I want to add items to my basket, enter my shipping details, and select delivery options so I can receive my order. | 1. Add merchandise to cart<br>2. Enter shipping details<br>3. Select delivery options<br>4. Complete order | Physical goods checkout process works | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Could Have_ priority - planned for Phase 3 |
| 3.2.2 | As a customer, I want to choose between standard and express shipping to control delivery time and cost. | 1. Add physical items to cart<br>2. View shipping options<br>3. Select preferred shipping<br>4. Verify cost calculation | Multiple shipping options available with pricing | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Could Have_ priority - planned for Phase 3 |

#### Epic 3.3: Admin Fulfilment

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 3.3.1 | As a site admin, I want to update stock levels and mark orders as shipped so customers stay informed. | 1. Log in as admin<br>2. Access order management<br>3. Update order status<br>4. Verify customer notification | Stock and shipping management functional | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Could Have_ priority - planned for Phase 3 |
| 3.3.2 | As a customer, I want to choose between standard and express shipping to control delivery time and cost. | 1. Add physical items to cart<br>2. View shipping options<br>3. Select preferred shipping<br>4. Verify cost calculation | Multiple shipping options available with pricing | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Could Have_ priority - planned for Phase 3 |

### Theme 4: Accounts & Authentication

#### Epic 4.1: Player Accounts

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 4.1.1 | As a customer, I want to register and log in with my email so I can access purchases and manage my account. | 1. Register new account<br>2. Verify email login<br>3. Access account dashboard<br>4. Manage account settings | User registration and login functional | ✅ Authentication system works | ✅ PASS | Full user authentication with Django Allauth |
| 4.1.2 | As a customer, I want to save my billing and shipping addresses for faster future checkouts. | 1. Add address to account<br>2. Save address<br>3. Use saved address in checkout<br>4. Verify faster checkout | Saved addresses work for faster checkout | ✅ Address management functional | ✅ PASS | Saved address functionality implemented |

#### Epic 4.2: Admin User Management

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 4.2.1 | As a site admin, I want to view registered users and manage roles so I can maintain store security. | 1. Log in as admin<br>2. Access user management<br>3. View user list<br>4. Manage user roles | Admin user management functional | ✅ User management works | ✅ PASS | Full user management in Django admin |

### Theme 5: Checkout & Payment

#### Epic 5.1: Secure Payments

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 5.1.1 | As a customer, I want to securely pay for items using Stripe so my payment details are protected. | 1. Add items to cart<br>2. Proceed to payment<br>3. Enter payment details<br>4. Complete secure payment | Stripe payment processing works securely | ✅ Stripe integration functional | ✅ PASS | Secure Stripe payment processing implemented |
| 5.1.2 | As a customer, I want to review my order summary and total cost before finalising payment so I can confirm my purchase. | 1. Add items to cart<br>2. Proceed to checkout<br>3. Review order summary<br>4. Confirm totals before payment | Order review with accurate totals | ✅ Order review works correctly | ✅ PASS | Comprehensive order review before payment |

#### Epic 5.2: Admin Order Oversight

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 5.2.1 | As a site admin, I want to see all orders and their payment statuses so I can troubleshoot and manage sales. | 1. Log in as admin<br>2. Access order management<br>3. View all orders<br>4. Check payment statuses | Complete order oversight for admin | ✅ Admin order management works | ✅ PASS | Full order management in Django admin |
| 5.2.2 | As a site admin, I want to process refunds for orders directly from the admin panel so I can resolve customer issues efficiently. | 1. Log in as admin<br>2. Access order<br>3. Process refund<br>4. Verify refund completion | Refund processing from admin panel | ⏸️ Basic functionality implemented | ⏸️ DEFERRED | _Should Have priority_ - basic tracking available. Foundation ready to implement full refund processing in Phase 2.  |

### Theme 6: Subscriptions

#### Epic 6.1: Player Subscription Management

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 6.1.1 | As a customer, I want to subscribe to Eclipse+ for monthly credits, DLC access, and perks so I can get ongoing benefits. | 1. Navigate to subscription page<br>2. Select subscription plan<br>3. Complete subscription signup<br>4. Verify benefits access | Subscription system functional with benefits | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Should Have_ priority - planned for Phase 2 |
| 6.1.2 | As a customer, I want to manage or cancel my subscription from my account dashboard so I remain in control. | 1. Log into account<br>2. Access subscription management<br>3. Modify or cancel subscription<br>4. Verify changes applied | Subscription self-management available | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Should Have_ priority - planned for Phase 2 |

#### Epic 6.2: Admin Subscription Oversight

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 6.2.1 | As a site admin, I want to view current subscribers and renewal statuses so I can manage billing effectively. | 1. Log in as admin<br>2. Access subscription management<br>3. View subscriber list<br>4. Check renewal statuses | Admin subscription oversight functional | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Should Have_ priority - planned for Phase 2 |

### Theme 7: Admin Analytics

#### Epic 7.1: Sales & Performance Insights

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 7.1.1 | As the business owner, I want to see total revenue and best-selling products so I can track performance. | 1. Log in as admin<br>2. Access analytics dashboard<br>3. View revenue metrics<br>4. Check best-selling products | Analytics dashboard with sales insights | ⏸️ Not implemented | ⏸️ DEFERRED | _Won't Have_ priority - future consideration |
| 7.1.2 | As the business owner, I want to view sales data by platform (Steam, Xbox, PlayStation) so I can adjust marketing strategies. | 1. Access analytics<br>2. Filter by platform<br>3. View platform-specific data<br>4. Analyse marketing insights | Platform-specific analytics available | ⏸️ Not implemented | ⏸️ DEFERRED | _Won't Have_ priority - future consideration |

### Theme 8: Reviews & Community

#### Epic 8.1: Product Reviews

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 8.1.1 | As a customer, I want to leave a rating and review on products I've purchased so I can share my opinion. | 1. Purchase product<br>2. Navigate to product page<br>3. Leave review and rating<br>4. Verify review appears | Review system functional for purchased products | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Could Have_ priority - planned for Phase 3 |
| 8.1.2 | As a customer, I want to read reviews from other players before purchasing. | 1. Navigate to product page<br>2. View existing reviews<br>3. Read ratings and comments<br>4. Make informed decision | Product reviews visible to all customers | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Could Have_ priority - planned for Phase 3 |

#### Epic 8.2: Admin Review Moderation

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 8.2.1 | As a site admin, I want to moderate or remove inappropriate reviews. | 1. Log in as admin<br>2. Access review management<br>3. Moderate reviews<br>4. Remove inappropriate content | Review moderation tools available | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Could Have_ priority - planned for Phase 3 |

### Theme 9: Newsletter & Marketing

#### Epic 9.1: Newsletter Subscriptions

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 9.1.1 | As a customer, I want to subscribe to a newsletter for exclusive offers and updates. | 1. Find newsletter signup<br>2. Enter email address<br>3. Confirm subscription<br>4. Verify signup confirmation | Newsletter subscription system functional | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Should Have_ priority for Phase 2 |

#### Epic 9.2: Admin Newsletter Management

| Story No. | User Story | Test Steps | Expected Result | Actual Result | Status | Notes |
|-----------|------------|------------|-----------------|---------------|--------|-------|
| 9.2.1 | As a site admin, I want to manage active subscribers so I can send targeted promotions. | 1. Log in as admin<br>2. Access subscriber management<br>3. View subscriber list<br>4. Manage subscriber data | Newsletter management tools available | ⏸️ Not implemented in MVP | ⏸️ DEFERRED | _Should Have_ priority for Phase 2 |

### Summary of Testing Results

Following the comprehensive user story testing, the majority of core functionalities have been successfully implemented and verified. Key features such as product browsing, secure checkout, digital delivery, and user account management have passed all acceptance criteria. Following MoSCoW prioritisation, several 'Should Have' and 'Could Have' features have been deferred to future development phases to ensure timely delivery of the MVP. Overall, the testing phase has confirmed that the digital storefront meets the essential requirements for a functional and user-friendly experience.


