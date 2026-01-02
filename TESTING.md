Contents

1. [HTML Validation](#1-html-validation)
2. CSS Validation
3. JavaScript Validation
4. Python Code Quality
5. Lighthouse Performance Testing
6. WAVE Accessibility Testing
7. Responsiveness Design Testing
8. User Story Testing
9. Automated Testing
10. Manual Testing
- Navigation Testing
- Form Testing
- Defensive Programming Testing
- Authentication Security Testing
- Input Validation
11. AWS S3 Storage Testing
12. Fixed Issues
13. Bug Reporting

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
| [Search Results Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/search/?q=test) | `/search/` | ✅ | ![search results validation screenshot](docs/images/test-screenshots/search-results-html-validation.png) | [Search Results Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Fproducts%2Fsearch%2F) |  |
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



