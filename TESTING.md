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
| [Checkout Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/) | `/checkout/` | ✅ | ![checkout validation screenshot](docs/images/test-screenshots/checkout-html-validation.png) | Login required. Validated by text input |  |
| [Review Order Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/review/) | `/checkout/review/` | ✅ | ![review order validation screenshot](docs/images/test-screenshots/review-order-html-validation.png) | Login required. Validated by text input |  |
| [Payment Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/payment/) | `/checkout/payment/` | ✅ | ![payment page validation screenshot](docs/images/test-screenshots/payment-html-validation.png) | Login required. Validated by text input |  |
| [Order Confirmation Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/checkout/confirmation/) | `/checkout/confirmation/` | ✅ | ![order confirmation validation screenshot](docs/images/test-screenshots/order-confirmation-html-validation.png) | Login required. Validated by text input |  |
| [404 Error Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/nonexistentpage/) | `/nonexistentpage/` | ✅ | ![404 error page validation screenshot](docs/images/test-screenshots/404-html-validation.png) | Validated by text input |  |


**Notes:**
¹ **Login Page Language Warning:** W3C usually reports OK but occasionally flags the page as Norwegian due to automatic language detection. The page correctly uses `lang="en-GB"`, `LANGUAGE_CODE = 'en-gb'`, and `LocaleMiddleware` sends `Content-Language: en`. This intermittent issue matches a known validator [issue](https://github.com/validator/validator/issues/321). It mostly occurs on form pages with minimal text.

![login validation language warning screenshot](docs/images/test-screenshots/login-language-warning-html-validation.png)