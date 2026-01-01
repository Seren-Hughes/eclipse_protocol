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
| [Login Page](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/accounts/login/) | `/accounts/login/` | ✅ | ![login validation screenshot](docs/images/test-screenshots/login-html-validation.png) | [Login Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Feclipse-protocol-15d26c9e2a55.herokuapp.com%2Faccounts%2Flogin%2F) | ![login validation language warning screenshot](docs/images/test-screenshots/login-language-warning-html-validation.png) W3C usually reports ok but occasionally automatic language detection flags it incorrectly as Norwegian. HTML is correctly set to English (en-GB). Settings are also set to en-gb and added middleware `'django.middleware.locale.LocaleMiddleware'` is sending `Content-Language: en`. The warning appears intermittently and matches a known validator [issue](https://github.com/validator/validator/issues/321) . |
