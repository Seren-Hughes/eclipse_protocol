# Eclipse Protocol E-Commerce 

![Eclipse Protocol E-Commerce Banner](docs/images/screenshots/eclipse-protocol-presentation-screenshot.png)

### Tech Stack:

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2.7-092E20?style=flat&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=flat&logo=stripe&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-S3-FF9900?style=flat&logo=amazon-aws&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat&logo=javascript&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)

A fictional e-commerce platform for a speculative video game company, Dark Sky Games, selling digital products on a dedicated store for their game - Eclipse Protocol. 

[**Link to Eclipse Protocol E-Commerce Store**](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/)

Hosted on Heroku with eco dynos - initial load may take 10-15 seconds as dynos require wake-up time after periods of inactivity

## Project Purpose & Value Proposition

The in-game currency system for Eclipse Protocol is inspired by established models used in games such as Roblox (Robux) and Apex Legends (Apex Coins) by EA Games.
Virtual currencies have become a standard part of modern game economies, offering a consistent way to handle microtransactions, cosmetic content, and bundled purchases across platforms and regions.
Adopting a credit-based system in this project helps to replicate a realistic e-commerce flow while reflecting common monetisation structures found in contemporary digital game stores.

**Purpose:** To create a secure, user-friendly e-commerce platform that enables customers to purchase digital game content (license keys, in-game currency) while providing administrators with tools to manage products, orders, and customer relationships.

**Value to Users:**
- **Customers** can conveniently purchase and instantly access digital game content through a single platform, with their purchase history and license keys stored securely in their account dashboard
- **Site Administrators** gain management tools through Django's admin interface to handle product catalogues, process orders, manage license key inventory, and moderate user-generated content
- **Business Owner** benefits from a scalable platform that can grow from digital-only sales to include subscriptions, physical merchandise, and community features

**Technical Implementation:** This project demonstrates Django backend architecture, PostgreSQL relational database design, Stripe payment integration, AWS S3 storage, responsive frontend design with Bootstrap, and deployment to a production environment. The MVP focuses on core e-commerce functionality with digital product delivery, while the modular structure allows for future expansion into subscriptions, physical goods fulfilment, and advanced analytics.

# Contents:
1. [Wireframes](#wireframes)
2. [Colour Palette](#colour-palette)
3. [Accessibility & Contrast Testing](#contrast--accessibility)
4. [Typography](#typography)
5. [Project Management & Planning](#project-management--planning)
6. [User Stories by Theme and Epic](#user-stories-by-theme-and-epic)
7. [Effort Risk Fibonacci Matrix](#effort-risk-fibonacci-matrix)
8. [ERD Diagram](#erd-diagram)
9. [Site Map](#site-map)
10. [User Flow Diagrams](#user-flow-diagrams)
11. [Products & Catalogue Structure](#products--catalogue-structure)
12. [Technologies Used](#technologies-used)
13. [Site Features](#site-features)
14. [Testing](#testing)
15. [Deployment](#deployment)
16. [Credits & References](#credits--references)
17. [Acknowledgements](#acknowledgements)



# Wireframes:

## Product Pages

### Landing Page:

![Eclipse Protocol E-Commerce Landing Page](docs/images/wireframes/landing-page.png)

### Base Game Product Page:

![Eclipse Protocol E-Commerce Base Game Product Page](docs/images/wireframes/base-game-store.png)

### Edition Details:

![Eclipse Protocol E-Commerce Edition Details](docs/images/wireframes/edition-detail.png)

### DLC Product Page:

![Eclipse Protocol E-Commerce DLC Product Page](docs/images/wireframes/dlc-product-page.png)

### Eclipse Plus Subscription Page:

![Eclipse Protocol E-Commerce Eclipse Plus Subscription Page](docs/images/wireframes/eclipse-plus-subscription.png)

### Subscription Payment Page:

![Eclipse Protocol E-Commerce Subscription Payment Page](docs/images/wireframes/subscription-payment-page.png)

### Game Currency Details Page:

![Eclipse Protocol E-Commerce Game Currency Details Page](docs/images/wireframes/game-currency-details.png)

### Search Results Page:

![Eclipse Protocol E-Commerce Search Results Page](docs/images/wireframes/search-results-page.png)

### Merchandise Product Page:

![Eclipse Protocol E-Commerce Merchandise Product Page](docs/images/wireframes/merchandise-product-page.png)

### Merchandise Detail Page:

![Eclipse Protocol E-Commerce Merchandise Detail Page](docs/images/wireframes/merchandise-detail-page.png)

## Account & Authentication

### Sign In Page:

![Eclipse Protocol E-Commerce Sign In Page](docs/images/wireframes/sign-in-page.png)

### Create Account Page:

![Eclipse Protocol E-Commerce Create Account Page](docs/images/wireframes/create-account-page.png)

### User Account: 

![Eclipse Protocol E-Commerce User Account Page](docs/images/wireframes/user-account-page.png)

### Wishlist Page:

![Eclipse Protocol E-Commerce Wishlist Page](docs/images/wireframes/wishlist-page.png)

## Shopping & Checkout

### Cart Page:

![Eclipse Protocol E-Commerce Cart Page](docs/images/wireframes/cart-page.png)

**Note on Checkout Flow:**
The checkout process designs will use conditional logic based on cart contents:
- **Digital-only purchases** follow a streamlined 2-step process (Review Order → Payment)
- **Physical merchandise purchases** include an additional Shipping Details step (Billing & Shipping → Review Order → Payment)
- **MVP design** focuses on digital sales, with physical merchandise checkout flow to be expanded in future iterations.

These designs ensure customers purchasing digital products (game keys, DLC, credits) experience a faster checkout, while physical merchandise orders collect necessary shipping information.

### Payment/Billing MVP Page:

![Eclipse Protocol E-Commerce Payment Billing Page](docs/images/wireframes/payment-billing-page-mvp.png)

### Billing and Shipping Details Page:

![Eclipse Protocol E-Commerce Billing and Shipping Details Page](docs/images/wireframes/billing-shipping-details.png)

**Note:** The following wireframes show the variations in the billing and shipping addresses expanded forms for different scenarios:

![Billing and Shipping Multi Laptop Option Views](docs/images/wireframes/billing-shipping-multi-laptop-option-views.png)

![Billing and Shipping Method](docs/images/wireframes/billing-shipping-method.png)

![Billing and Shipping Review Order](docs/images/wireframes/billing-shipping-review-order.png)

![Billing and Shipping Payment](docs/images/wireframes/billing-shipping-payment.png)

### Digital Sale Only Billing:

![Eclipse Protocol E-Commerce Digital Sale Only Billing](docs/images/wireframes/digital-sale-only-billing.png)

![Digital Sale Only Review Order](docs/images/wireframes/digital-sale-only-review-order.png)

![Digital Sale Only Payment](docs/images/wireframes/digital-sale-only-payment.png)

### Order Confirmation of Purchase Page:

![Eclipse Protocol E-Commerce Order Confirmation of Purchase Page](docs/images/wireframes/order-confirmation-page.png)

## Support & Information Pages

### Contact/Support Page:

![Eclipse Protocol E-Commerce Contact/Support Page](docs/images/wireframes/contact-support-page.png)

### Confirmation Contact/Support Submission Page:

![Eclipse Protocol E-Commerce Confirmation Contact/Support Submission Page](docs/images/wireframes/confirmation-contact-submission.png)

### Information Pages: 

![Eclipse Protocol E-Commerce Information Pages](docs/images/wireframes/information-pages.png)

### Error 404 Page:

![Eclipse Protocol E-Commerce Error 404 Page](docs/images/wireframes/error-page.png)

## Colour Palette:

![Eclipse Protocol E-Commerce Colour Palette](docs/images/design/eclipse-protocol-colour-pallette.png)

#### Contrast & Accessibility:

The Eclipse Protocol colour palette has been designed with accessibility in mind, ensuring sufficient contrast ratios for users with visual impairments and colour vision differences. The site employs a dark theme with generous use of clean negative space, creating a visually striking but uncluttered interface that prioritises readability and user focus.

**Contrast Testing:**
- All text/background combinations tested using [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- Meets WCAG 2.1 AA compliance standards for normal and large text
- Primary white text (`#ffffff`) tested against all dark background variations

<details>
<summary><em>Click to expand</em><br>
WebAIM contrast ratio verification screenshots for primary text combinations
</summary>

**Primary Text (#ffffff) vs Background Variations:**
- Against main background (`#0b0c0e`): [19.56:1]
- Against charcoal (`#202122`): [16.12.1]  
- Against dark grey (`#45464a`): [9.42:1]

![WebAIM contrast test - main background](docs/images/design/contrast-test-main-bg.png)
![WebAIM contrast test - charcoal background](docs/images/design/contrast-test-charcoal.png)
![WebAIM contrast test - dark grey background](docs/images/design/contrast-test-dark-grey.png)
</details>
<br>

**Colour Vision Support:**
- Site tested with Colorblindly browser extension to verify usability for users with colour vision differences
- Information conveyed through colour is supplemented with text labels and [Font Awesome](https://fontawesome.com/) iconography
- Interactive elements maintain clear visual distinction across all colour vision types

**Monochrome Testing:**
![Eclipse Protocol site in monochrome view](docs/images/design/monochrome-eclipse-protocol-screenshot.png)
_Site tested in monochrome to verify information hierarchy and usability without colour dependency._

![Eclipse Protocol Game selection screen in monochrome view](docs/images/design/monochrome-game-product-page-screenshot.png)
_Selection screen tested in monochrome to ensure product differentiation remains clear._

**Design Philosophy & Accessibility:**
The dark theme incorporates extensive clean negative space, creating visual breathing room that enhances readability and reduces cognitive load. This minimalist approach ensures content hierarchy remains clear while maintaining the futuristic aesthetic appropriate for a space-themed gaming platform.

**Additional Accessibility Features:**
- Semantic HTML structure with proper heading hierarchy
- Alt text provided for all informational images
- Focus indicators maintained for keyboard navigation
- Form labels properly associated with input elements

_Full accessibility testing results documented in [TESTING.md](TESTING.md#5-lighthouse-performance-testing)._

## Typography:

Eclipse Protocol utilises carefully selected Google Fonts to maintain readability while reinforcing the futuristic gaming aesthetic.

**Primary Font: [Arimo](https://fonts.google.com/specimen/Arimo)**
- Used for body text, navigation, and general content
- Sans-serif design optimised for screen readability
- Weight range: 400-700 (regular to bold) with italic variants
- Fallback: Arial, sans-serif for maximum compatibility

**Secondary Font: [Oswald](https://fonts.google.com/specimen/Oswald)**
- Used for headings, product titles, and emphasis text
- Condensed sans-serif with strong visual impact
- Weight range: 200-700 (light to bold)
- Fallback: Verdana, sans-serif for reliable display

<details>
<summary><em>Click to expand</em><br>
Google Fonts selection and preview screenshots
</summary>

**Arimo Font Preview:**
![Arimo font preview from Google Fonts](docs/images/design/arimo-font-preview.png)
**Oswald Font Preview:**
![Oswald font preview from Google Fonts](docs/images/design/oswald-font-preview.png)
</details>
<br>

**Font Loading & Performance:**
- Google Fonts loaded via CSS `@import` with `display=swap` parameter
- Font-display: swap ensures faster initial page render with fallback fonts
- Weight ranges optimised to load only required font variations
- Fallback fonts ensure content remains accessible if web fonts fail to load

**Implementation:**
Included in [variables.css](static/css/variables.css) for consistent use across the application:

```css
@import url('https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400..700;1,400..700&family=Oswald:wght@200..700&display=swap');
```

**Design Rationale:**
- Arimo's clean geometry supports the futuristic aesthetic while maintaining excellent readability
- Oswald's condensed form is ideal for alternate headings and product titles and complements Arimo without visual clash 
- Both fonts maintain legibility across devices and screen sizes

**Accessibility Considerations:**
- Both fonts tested for legibility at various sizes
- Sufficient x-height and character spacing for dyslexic users
- Clean letterforms reduce cognitive load for extended reading
- CSS variables enable consistent typography throughout the application

## GitHub Projects & Agile Implementation

### Project Management Methodology
This project utilised GitHub Projects with an agile approach, implementing MoSCoW prioritisation (Must Have, Should Have, Could Have, Won't Have) combined with iterative development cycles focused on delivering a functional e-commerce platform.

[Link to the Eclipse Protocol Project Board](https://github.com/users/Seren-Hughes/projects/9) 

### GitHub Projects Kanban Board
<details>
<summary><em>Click to expand</em><br>
MoSCoW prioritised user stories for digital e-commerce platform tracked through GitHub Projects with clear priority labels and epic organisation
</summary>

![GitHub Projects Kanban Board](docs/images/screenshots/moscow-kanban-board.png)
</details>

### GitHub Issues & Milestones
<details>
<summary><em>Click to expand</em><br>
User stories broken down into manageable issues with story points, linked to milestones for sprint planning and progress tracking. Labels used for priority and epic categorisation.
</summary>

![GitHub Issues & Milestones](docs/images/screenshots/issue-labelling.png)
</details>

### Sprint Planning & Management

**Sprint 1-2: Foundation & Authentication** *(Milestone: User Management)*
- Django project setup and PostgreSQL configuration
- User registration, login, and logout functionality
- User profile model with address management
- Custom authentication forms and validation

**Sprint 3-4: Product Catalogue & Variants** *(Milestone: Digital Storefront)*
- Product model with type-based extensions
- Digital variant system for platform/edition combinations
- Currency product management for credit packs
- Admin interface for product creation and management

**Sprint 5-6: Shopping Cart & Checkout** *(Milestone: E-Commerce Core)*
- Shopping cart with session persistence and user migration
- Wishlist functionality with AJAX toggles
- Checkout flow with address handling and validation
- Order confirmation system with email notifications

**Sprint 7-8: Payment Processing & Digital Delivery** *(Milestone: Secure Transactions)*
- Stripe payment integration with webhook handling
- Secure payment forms with client-side validation
- License key generation system with UUID implementation
- Order status tracking and automated digital delivery

**Sprint 9-10: Admin Tools & Support** *(Milestone: Management System)*
- Django admin customisation for product and order management
- Custom sales dashboard with revenue analytics
- Customer support contact system with categorisation
- License key tracking and delivery status monitoring

**Sprint 11-12: Testing & Production Deployment** *(Milestone: Release 1 MVP)*
- Comprehensive unit and integration testing
- AWS S3 integration for static and media files
- Heroku production deployment and environment configuration
- Final bug fixes and performance optimisations

**Deferred Features: Advanced E-Commerce** *(Planned for Release 2)*
- Eclipse+ subscription billing with Stripe recurring payments
- Physical merchandise support with inventory management
- Shipping calculation and fulfilment workflow
- Newsletter subscription management
- Advanced analytics dashboard with customer behaviour tracking
- Product review and rating system

### Development Reality vs Planning

While the sprint structure above represents the planned development sequence, actual implementation followed a more iterative approach typical of agile development. Features were developed incrementally with some parallel work on foundational elements (authentication, models) and integration components (Stripe, AWS) happening across multiple sprints as dependencies were discovered and technical requirements evolved.

This iterative approach allowed for:
- Early testing of payment integration
- Continuous refinement of the product model architecture
- Responsive adjustment to technical challenges
- Better integration between frontend and backend components

### Agile Development Impact

The agile approach enabled rapid iteration and continuous delivery of e-commerce functionality. Regular sprint retrospectives allowed for strategic feature prioritisation, leading to the deferral of subscription billing and physical merchandise to future releases. This ensured that core digital commerce functionality was delivered within the MVP timeline.

The MoSCoW framework proved particularly effective for e-commerce development, allowing clear distinction between essential payment processing features (Must Have) and enhancement features like reviews and analytics (Could Have).

## User Stories by Theme and Epic:

### Theme 1: Digital Storefront
#### Epic 1.1: Browse & Discover Digital Products
|Story No. |User Story |Story Points |Priority |
|-------------------|------------------------|----|--------------|
| 1.1.1	 | As a customer, I want to browse all available digital products (base game, DLC, credits etc.) so I can see what's available for my platform. |	5 |	Must Have |
| 1.1.2	 | As a customer, I want to filter digital items by platform (Steam, Xbox, Nintendo, PlayStation) so I only see compatible content. |	3 |	Should Have |
| 1.1.3	 | As a customer, I want to sort or filter by relevance or price so I can easily find what I want. |	3 |	Should Have |

#### Epic 1.2: Product Details
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 1.2.1	 | As a customer, I want to view detailed product pages with descriptions, editions, prices, and platform options so I can make informed decisions. |	5 |	Must Have |
| 1.2.2	 | As a customer, I want to see information on delivery method (redeemable key or automatic activation) before purchase. |	5 |	Must Have |

#### Epic 1.3: Product Management (Admin)
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 1.3.1	 | As a site admin, I want to create, edit, and delete product listings so I can manage the catalogue easily. |	8 |	Must Have |

### Theme 2: Digital Checkout & Delivery
#### Epic 2.1: Purchase & Payment
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 2.1.1	 | As a customer, I want to add digital items to my basket and securely purchase them so I can access them in my account. |	8 |	Must Have |
| 2.1.2	 | As a customer, I want to view an order summary and confirm before paying. |	3 |	Must Have |

#### Epic 2.2: Delivery & Key Management
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 2.2.1	 | As a customer, I want my digital key or credits to be automatically applied to my account and emailed after purchase. |	8 |	Must Have |

#### Epic 2.3: Order History
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 2.3.1	 | As a customer, I want to view my order history with product names, dates, and total amounts so I can track past purchases. |	5 |	Must Have |

#### Epic 2.4: License Management (Admin)
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 2.4.1	 | As a site admin, I want to manage license key generation and mark keys as redeemed so availability stays accurate. |	5 |	Must Have |

### Theme 3: Merchandise Store
#### Epic 3.1: Browse & Purchase Merchandise
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 3.1.1	 | As a customer, I want to browse official merchandise (t-shirts, hoodies, mugs) so I can support the brand I enjoy. |	3 |	Could Have |

#### Epic 3.2: Checkout & Delivery
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 3.2.1	 | As a customer, I want to add items to my basket, enter my shipping details, and select delivery options so I can receive my order. |	8 |	Could Have |
| 3.2.2	 | As a customer, I want to choose between standard and express shipping to control delivery time and cost. |	3 |	Could Have |

#### Epic 3.3: Admin Fulfilment
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 3.3.1	 | As a site admin, I want to update stock levels and mark orders as shipped so customers stay informed. |	5 |	Could Have |

### Theme 4: Accounts & Authentication
#### Epic 4.1: Player Accounts
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 4.1.1	 | As a customer, I want to register and log in with my email so I can access purchases and manage my account. |	5 |	Must Have |
| 4.1.2	 | As a customer, I want to save my billing and shipping addresses for faster future checkouts. |	3 |	Should Have |

#### Epic 4.2: Admin User Management
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 4.2.1	 | As a site admin, I want to view registered users and manage roles so I can maintain store security. |	5 |	Must Have |

### Theme 5: Checkout & Payment
#### Epic 5.1: Secure Payments
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 5.1.1	 | As a customer, I want to securely pay for items using Stripe so my payment details are protected. |	8 |	Must Have |
| 5.1.2	 | As a customer, I want to review my order summary and total cost before finalising payment so I can confirm my purchase. |	3 |	Must Have |

#### Epic 5.2: Admin Order Oversight
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 5.2.1	 | As a site admin, I want to see all orders and their payment statuses so I can troubleshoot and manage sales. |	5 |	Must Have |
| 5.2.2	 | As a site admin, I want to process refunds for orders directly from the admin panel so I can resolve customer issues efficiently. |	5 |	Should Have |

### Theme 6: Subscriptions
#### Epic 6.1: Player Subscription Management
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 6.1.1	 | As a customer, I want to subscribe to Eclipse+ for monthly credits, DLC access, and perks so I can get ongoing benefits. |	8 |	Should Have |
| 6.1.2	 | As a customer, I want to manage or cancel my subscription from my account dashboard so I remain in control. |	5 |	Should Have |

#### Epic 6.2: Admin Subscription Oversight
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 6.2.1	 | As a site admin, I want to view current subscribers and renewal statuses so I can manage billing effectively. |	5 |	Should Have |

### Theme 7: Admin Analytics
#### Epic 7.1: Sales & Performance Insights
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 7.1.1	 | As the business owner, I want to see total revenue and best-selling products so I can track performance. |	5 |	Won't Have |
| 7.1.2	 | As the business owner, I want to view sales data by platform (Steam, Xbox, PlayStation) so I can adjust marketing strategies. |	5 |	Won't Have |

### Theme 8: Reviews & Community
#### Epic 8.1: Product Reviews
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 8.1.1	 | As a customer, I want to leave a rating and review on products I've purchased so I can share my opinion. |	5 |	Could Have |
| 8.1.2	 | As a customer, I want to read reviews from other players before purchasing. |	3 |	Could Have |

#### Epic 8.2: Admin Review Moderation
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 8.2.1	 | As a site admin, I want to moderate or remove inappropriate reviews. |	3 |	Could Have |

### Theme 9: Newsletter & Marketing
#### Epic 9.1: Newsletter Subscriptions
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 9.1.1	 | As a customer, I want to subscribe to a newsletter for exclusive offers and updates. |	5 |	Should Have |

#### Epic 9.2: Admin Newsletter Management
| Story No. |	User Story |	Story Points |    Priority |
|-----------|-------------|---------------|--------------|
| 9.2.1	 | As a site admin, I want to manage active subscribers so I can send targeted promotions. |	5 |	Should Have |


## Effort Risk Fibonacci Matrix:

![Eclipse Protocol E-Commerce Effort Risk Fibonacci Matrix](docs/images/diagrams/effort-risk-matrix.png)

The Effort Risk Fibonacci Matrix was created in Miro using digital post-it notes, with user stories colour-coded according to MoSCoW prioritisation. This visual planning tool helped map story points against implementation risk, allowing for informed iteration planning. The digital format made it easy to adjust and reorganise stories as project requirements evolved during development.

Low-risk stories were prioritised for early sprints to establish core functionality, while high-risk items were tackled incrementally with sufficient time allocated for problem-solving and testing.

## ERD Diagram:

![Eclipse Protocol E-Commerce ERD](docs/images/diagrams/eclipse-protocol-erd.png)

_(Zoomable version available at: docs/images/diagrams/eclipse-protocol-erd.png or open image in new tab for larger view)_

### Database Design (ERD Overview)

The Eclipse Protocol database is designed around a digital e-commerce platform with support for user accounts, product variants, orders, and customer support. The current implementation focuses on digital product sales with a flexible architecture that can accommodate future physical merchandise and subscription services.

#### Current MVP Implementation

**User Management:**
- `users` - Django's built-in authentication (email, username, password, permissions)
- `user_profiles` - Extended user data (names, phone, default address reference)
- `addresses` - User billing/shipping addresses with type designation and address snapshots for order history preservation

**Product Catalog:**
- `products` - Base catalogue entries for all sellable items (name, price, product_type, SKU, images)
- `digital_variants` - Platform/edition combinations for base games (PC/Xbox/Nintendo × Standard/Premium/Ultimate editions with individual pricing and descriptions)
- `currency_products` - Credit pack configurations (100-10,000 credits with pricing tiers)
- `digital_products` - Simple digital items for future DLC/expansion content

**Shopping & Orders:**
- `cart_items` - Shopping cart with support for product variants and quantity management
- `wishlists` - User product favorites for future purchase
- `orders` - Complete order records with billing/shipping snapshots and Stripe payment integration
- `order_items` - Individual line items preserving product/variant details and historical pricing
- `license_keys` - Digital delivery system with platform-specific key generation and user account integration

**Customer Support:**
- `contact_messages` - Support ticket system with categorisation, status tracking, and admin workflow management

**Key Implementation Details:**

*License Key Generation:* Keys are generated on-demand via UUID when payment succeeds rather than managing a pre-generated inventory pool. This approach keeps the implementation simple while simulating realistic digital delivery without the complexity of stock management.

*Address Snapshots:* Order records preserve billing/shipping information at time of purchase to maintain historical accuracy even when users update their saved addresses. This prevents order history from changing retroactively while still allowing convenient navigation to current user addresses.

*Product-Variant Architecture:* The system uses a flexible base Product model with specialised variants for base games (DigitalVariant) and extensions for other types (CurrencyProduct, DigitalProduct). This allows complex platform/edition combinations while maintaining clean separation of concerns.

#### Future Development Phases

**Newsletter & Marketing** - Newsletter subscription management with guest email support and targeted communication capabilities for promotional campaigns and game updates.

**Subscription Services** - Eclipse+ membership plans with recurring billing, exclusive content access, monthly credit allocation, and subscriber perk management through Stripe's subscription billing system.

**Physical Merchandise** - Apparel and collectibles with size/colour variant management, inventory tracking, shipping calculations, and fulfilment workflow integration for branded products.

**Advanced Analytics** - Revenue reporting, platform performance tracking, customer behaviour analysis, and sales optimisation tools for business intelligence and marketing strategy development.

## Site Map:

```
Home Page (/)
│
├── Products (/products/)
│   ├── Search Results (/products/search/)
│   ├── Base Game (/products/base-game/eclipse-protocol/)
│   │   └── Platform/Edition Variants (/products/base-game/eclipse-protocol/{platform}/{edition}/)
│   └── Credits (/products/currency/)
│       └── Specific Credit Pack (/products/currency/{product-slug}/)
│
├── Shopping Cart (/cart/)
│
├── Authentication (/accounts/)
│   ├── Login (/accounts/login/)
│   ├── Logout (/accounts/logout/)
│   ├── Sign-up (/accounts/signup/)
│   │
│   └── (After login) →
│       │
│       ├── Account Dashboard (/accounts/) - Order History
│       ├── Order Details (/accounts/orders/{order-number}/)
│       ├── Saved Addresses (/accounts/addresses/)
│       │   ├── Add Address (/accounts/addresses/add/)
│       │   ├── Edit Address (/accounts/addresses/{id}/edit/)
│       │   └── Delete Address (/accounts/addresses/{id}/delete/)
│       │
│       └── Checkout (Login Required) (/checkout/)
│           ├── Review Order (/checkout/review/)
│           ├── Payment (/checkout/payment/)
│           ├── Process Payment (/checkout/process-payment/)
│           ├── Success (/checkout/success/{order-number}/)
│           └── Stripe Webhook (/checkout/webhook/)
│
├── Wishlist (/wishlist/) - Login Required
│
├── Support Pages (/pages/)
│   ├── Contact Form (/pages/contact/)
│   ├── Contact Confirmation (/pages/contact-confirmation/)
│   ├── About Us (/pages/about/)
│   ├── FAQs (/pages/faqs/)
│   ├── Privacy Policy (/pages/privacy-policy/)
│   └── Terms & Conditions (/pages/terms-and-conditions/)
│
├── Django Admin Panel (/admin/) - Staff Only
├── Admin Sales Dashboard (/admin-dashboard/) - Staff Only
│
└── Error Pages
    └── 404 Page Not Found
```

**Key Implementation Notes:**
- **No "All Products" listing** - Users browse via specific product types (base game vs currency)
- **No DLC or Merchandise** - MVP focuses on base game variants and credit packs
- **No Eclipse+ Subscription** - Planned for future development 
- **Simplified Product Structure** - Two main product types: base game with variants, currency packs
- **Streamlined Navigation** - Header focuses on "Buy Game" and "Buy Credits" direct links
- **Support Integration** - All support/information pages under `/pages/` URL namespace
- **Admin Dashboard** - Custom sales analytics separate from Django admin
- **Wishlist** - Both standalone page and AJAX toggle functionality
- **Address Management** - Full CRUD operations for user addresses

**Authentication Flow:**
- Product browsing is public for discovery
- Cart viewing is public, checkout requires login
- Wishlist requires login - guests redirected with return URL
- Account features only accessible to authenticated users

## Site Map Diagram:

![Eclipse Protocol E-Commerce Site Map](docs/images/diagrams/eclipse-protocol-site-map.png)

## User Flow Diagrams:

### Digital Product Purchase Flow:

![Eclipse Protocol E-Commerce Digital Product Purchase Flow](docs/images/diagrams/digital-product-purchase-flow.png) 

### Registration & Login Flow:

![Eclipse Protocol E-Commerce Registration and Login Flow](docs/images/diagrams/registration-login-flow.png)

### Admin Product Management Flow:

![Eclipse Protocol E-Commerce Admin Product Management Flow](docs/images/diagrams/admin-product-management-flow.png)


## Products & Catalogue Structure

The store sells both digital and physical products related to Eclipse Protocol. For the MVP, the priority will be on the digital side - in-game currency and the base game license system. 

As the game is fictional, all products and prices are speculative and displayed in GBP (£). In a real commercial release, regional pricing and automatic tax calculation (such as VAT for digital goods in the UK/EU, or sales tax in the US) would be implemented based on the customer's location. Stripe Tax could be integrated for this purpose. This functionality is outside the scope of the MVP but is noted here to reflect awareness of real-world e-commerce practices.

### Digital Products (MVP Focus)

#### 1. In-Game Currency Packs

Cross-platform credits that apply to the player's account when purchased.

| Credits | Price |
|---------|-------|
| 100 | £1.99 |
| 500 | £7.99 |
| 1,200 | £14.99 |
| 2,500 | £24.99 |
| 5,000 | £39.99 |

For this portfolio project, the credit delivery simulates how modern games like Roblox, Fortnite, and Apex Legends handle cross-platform virtual currency. In these systems, credits purchased through web stores are automatically applied to the player's account and synced across all platforms where they play.

The system demonstrates instant credit allocation to the customer's account upon successful payment, with email confirmation and purchase records stored for transaction history and customer support purposes. While no actual game API integration exists, this replicates the experience players expect when purchasing virtual currency - immediate availability across platforms without manual redemption steps.

_**Note:** In a production environment, this would require integration with the game's backend API to update player account balances and sync data across gaming platforms._

#### 2. Base Game (License Keys)

Sold in platform-specific editions, each with its own license key.

| Edition | Price | Platforms |
|---------|-------|-----------|
| Standard | £49.99 | PC (Steam), Xbox, Nintendo |
| Premium | £59.99 | PC (Steam), Xbox, Nintendo |
| Ultimate | £69.99 | PC (Steam), Xbox, Nintendo |

**PlayStation:** _Links externally to the official PlayStation Store for realism as PlayStation does not support third-party license key sales._

Each platform version and edition is stored as a separate product with a unique SKU and license key.

**License Delivery:** The license key is shown in the user dashboard and emailed after checkout.

**Base Game Licence Keys Implementation Details:**

In real-world game distribution, platform licence keys are allocated by the platforms themselves (Steam, Xbox Live, Nintendo eShop) to authorised retailers and developers. The game company receives batches of pre-generated keys from each platform which are then distributed through their store or retail partners.

For this portfolio project, the system simulates this process by generating unique licence keys on-demand using UUID patterns when payment succeeds. While this differs from the industry practice of managing pre-allocated key inventories from major platforms, it demonstrates the core e-commerce workflow: secure payment processing, key assignment to customer accounts, and automated digital delivery via email and account dashboard.

Keys are stored in the license_keys table, linked to the specific order item and user, and displayed in the user's account as well as included in confirmation emails. This approach keeps the implementation focused on demonstrating e-commerce fundamentals while acknowledging the more complex inventory management that would be required in a production environment.

_**Note:** In a live system, integration with platform APIs (Steam Partner API, Xbox Live, etc.) would be required to manage actual key inventories and validate key redemption status._

#### 3. DLC Packs (Could Have)

Optional future add-ons such as weapon skins, spacecraft customisation, and story expansions.

### Physical Merchandise (Could Have)

If there's time after the MVP is complete:
- Branded apparel (t-shirts, hoodies)
- Collectibles (mugs, posters)
- Limited edition items

### Eclipse+ Subscription (Should Have)

**Monthly: £9.99** | **Annual: £99.99** (save 17%)

**Subscriber Perks:**
- 1,000 monthly credits
- Exclusive DLC
- Early access to new content
- 10% in-game item discount
- Unlimited storage for game resources (loot, building materials, etc.)

**Implementation:** Stripe recurring billing planned for Phase 2, not part of MVP scope as it requires more complex backend integration for recurring Stripe payments.

---

### MVP Product Scope

| Included in MVP | Reason |
|----------------|--------|
| 5 × Credit Packs | Simple to implement, instant digital delivery  with email and account confirmation |
| 9 × Game Edition/Platform combinations - Standard, Premium, Ultimate for PC, Xbox, Nintendo | Demonstrates license-key purchase and platform variation |
| License-Key Generation + Email Delivery | Required to show purchase confirmation and digital fulfilment |

**Total MVP Products: ~14 SKUs** (5 credit packs + 9 platform editions)


## Technologies Used:

### Languages & Frameworks
**HTML5** - Semantic structure and content for e-commerce pages  
**CSS3** - Styling and responsive layouts
**JavaScript (ES6+)** - Client-side interactivity, AJAX cart operations, and dynamic functionality  
**Python 3.12** - Backend application logic and e-commerce business rules  
**Django 5.2.7** - Full-stack web framework with ORM, templating, and admin interface  

### Frontend Technologies & UI
**Bootstrap 5** - Responsive CSS framework and component library  
**Google Fonts** - Typography (Arimo, Oswald)  
**Font Awesome** - Iconography for UI elements and navigation  
**CSS Custom Properties** - Design system variables for consistent theme across the site  

### JavaScript APIs & Browser Features
**Fetch API** - Modern AJAX for cart updates and wishlist management  
**Stripe Elements** - Secure payment form integration  
**Bootstrap Modal & Toast API** - Enhanced UI feedback and confirmation dialogs  

### Backend & Database
**PostgreSQL** - Primary relational database for e-commerce data (via psycopg2 2.9.11)  
**Django ORM** - Object-relational mapping for product variants and order management  
**Django Signals** - Automated license key generation and order processing  
**dj-database-url 3.0.1** - Database configuration management  

### Authentication & Security
**Django Authentication** - Custom user model with email-based login  
**Custom Form Validation** - Multi-layered security for checkout and user data  
**CSRF Protection** - Built-in Django security for form submissions  
**Stripe Webhooks** - Secure payment confirmation and order processing  

### E-Commerce & Payment Processing
**Stripe 14.0.1** - Payment processing, webhook handling, and transaction management  
**Django Countries 8.2.0** - Country field support for billing addresses  
**UUID Generation** - Secure license key creation for digital products  

### Cloud Services & Storage
**AWS S3** - Cloud storage for product images and static files  
**Boto3 1.41.5** - AWS SDK for Python file management  
**Django Storages 1.14.6** - Custom storage backends for S3 integration  

### File Processing & Media
**Pillow 12.0.0** - Image processing and validation for product images       
**cwebp** - Command-line WebP encoder for optimising image file sizes and web performance

### Development & Deployment
**GitHub** - Version control and repository management  
**VSCode** - Code editing and development environment  
**Heroku** - Application hosting and deployment  
**Gunicorn 23.0.0** - WSGI HTTP server for production  
**Whitenoise 6.11.0** - Static file serving in production  

### Code Quality Tools
**Black 25.12.0** - Python code formatter  
**Flake8 7.3.0** - Python linting and style guide enforcement  
**isort 7.0.0** - Python import statement sorting  
**djlint 1.36.4** - Django template linting and formatting  
**Coverage 7.13.1** - Test coverage analysis  

### Testing & Quality Assurance
**Django TestCase** - Unit and integration testing framework  
**Coverage.py** - Code coverage measurement and reporting  
**Manual Testing** - Cross-browser compatibility and user experience validation  
**Google Lighthouse** - Performance, accessibility, and SEO auditing       
**BrowserStack** - Cross-browser testing and compatibility checks

### Project Management & Design Tools
**GitHub Projects** - Agile project management with MoSCoW prioritisation  
**Miro** - Brainstorming, user story mapping and effort-risk matrix creation  
**Balsamiq** - UI/UX wireframing and design                     
**WebAIM Contrast Checker** - Accessibility compliance testing  
**Colorblindly** - Colour vision difference simulation  

### Additional Development Tools
**ChatGPT** - Used alongside traditional documentation and for assisting written content to improve clarity   
**[drawdb](https://www.drawdb.app/)** - Database design and ERD documentation  
**Coolors** - Colour palette generation and design harmony                
**Adobe Photoshop** - Image editing and optimisation for web assets           


### Email Services
**[Catchmail](https://catchmail.io/)** - Temporary email service for testing email functionality without using real addresses                                                  
**Gmail SMTP** - Transactional email delivery for order confirmations, license key distribution, and customer communications

## Site Features

### Homepage & Navigation
- Hero section with product carousel
- Responsive navigation with search functionality
- Featured products display
- Footer with quick links and social media icons

**Homepage Storefront Screenshot:**                                     
_featured products selected by admin are displayed prominently for user engagement._

![Home Page Storefront](docs/images/screenshots/desktop-home-page.png)

**Responsive Navigation Bar Screenshot:**
_navigation adapts for mobile and desktop with collapsible menu._

![Responsive Navigation Bar](docs/images/screenshots/responsive-navigation.png)

### Product Catalogue & Discovery
- Game editions with platform variants (PC, Xbox, Nintendo)
- Currency packs with instant delivery
- Basic search functionality

**Product Display with Image Fallbacks:**
- Dynamic product cards with responsive layouts
- **Fallback system for missing images**: Font Awesome icons automatically display when product images fail to load
  - Coins icon for currency products
  - Game controller icon for game products
- Platform-specific variants (PC, Xbox, Nintendo) with individual pricing
- PlayStation edition links externally to official store with a modal asking users to confirm redirection

**Credit Pack Product Page:**

![Credits Products Page](docs/images/screenshots/desktop-credits-product-page.png)

**Game Product Page with Variants:**

![Game Product Page](docs/images/screenshots/desktop-game-edition-page.png)

**PlayStation Edition External Link Modal:**

![PlayStation External Link Modal](docs/images/screenshots/playstation-modal.png)

**Search Results Pages:**

![Search Results Pages](docs/images/screenshots/desktop-search-results.png)

**Empty Search Results State:**
![Search Results Empty](docs/images/screenshots/desktop-search-empty.png)

**No Results Found State:**
![Search Results - No results](docs/images/screenshots/desktop-search-no-results.png)

<details>
<summary><strong>View Fallback Product Image Screenshots</strong></summary>

- Missing image fallback: Currency product with coin icon
![Currency Product without image fallback](docs/images/screenshots/credit-pack-without-image.png)

- Missing image fallback: Game product with controller icon
![Game Product without image fallback](docs/images/screenshots/game-without-image.png)
</details>


### Shopping Experience
- Dynamic shopping cart with AJAX updates
- Wishlist functionality with heart toggles
- Guest users prompted to log in for wishlist access
- Wishlist items removable via AJAX
- Wishlist items added to cart directly from wishlist page and removed automatically
- Persistent cart across sessions
- Guest session cart merging on login with notification of merged items and no duplicates

**Wishlist Page Screenshot:**
_wishlist count displayed in header_

![Wishlist Page](docs/images/screenshots/desktop-wishlist.png)

**Wishlist Heart Toggle Functionality:**
- Heart icon toggles filled/outlined state based on wishlist status
![Wishlist Heart Toggle](docs/images/screenshots/wishlist-heart-toggle.gif)

**Shopping Basket Page Screenshot:**

![Cart Page with Product](docs/images/screenshots/desktop-cart.png)

**Empty Shopping Basket State:**                                       
_When the cart is empty, a friendly message encourages users to continue shopping._

![Empty Basket State](docs/images/screenshots/desktop-empty-basket.png)



### Checkout & Payment Integration
- Secure Stripe payment processing
- Order review and confirmation
- Real-time form validation

**Billing Form Page:**

![Checkout Page](docs/images/screenshots/desktop-checkout-form.png)

**Review Order Page:**

![Review Order Page](docs/images/screenshots/desktop-review-order.png)

**Payment Page with Stripe:**

![Payment Page](docs/images/screenshots/desktop-payment.png)

### Digital Product Delivery
- Automatic license key generation (UUID-based)
- Keys formatted to match platform conventions (Steam, Xbox, Nintendo)
- Instant delivery via email and account dashboard with platform-specific instructions how to redeem

### Digital License Key Delivery
**Platform-Specific Key Generation:**
- **PC/Steam Format**: `XXXXX-XXXXX-XXXXX-XXXXX` (20 characters)
- **Xbox Format**: `XXXXX-XXXXX-XXXXX-XXXXX-XXXXX` (25 characters)
- **Nintendo Format**: `AAAA-BBBB-CCCC-DDDD` (16 characters)

Generated via [`_generate_key_code()`](checkout/webhook_handler.py#L197) with collision detection for uniqueness.

**License Key Display in User Account:**
_License keys are shown in the user's order history with copy-to-clipboard functionality for convenience._

![User Order History License key](docs/images/screenshots/desktop-orders-and-license-keys.png)

**License Key Delivery Email:**
_Confirmation email includes license key and platform-specific redemption instructions with consistent styling to match the website and branding._

<img src="docs/images/screenshots/email-order.png" alt="Email Order Confirmation Licence key" width="350"/>

**Order Success Page:**
_After successful payment, users see a summary of their order, including information to check emails and spam for digital product delivery and can also be found in the user account order history dashboard_

![Order Success Page](docs/images/screenshots/desktop-order-success.png)

### User Account Management
- Order history
- Saved addresses for faster checkout
- License key library with copy functionality

**Order History Page Screenshot:**

![User Order History Page](docs/images/screenshots/desktop-order-history.png)

<details><summary>Click to View Order History Page with no orders</summary>

_Call to action for first purchase when no orders exist_

![Order History Empty State](docs/images/screenshots/desktop-account-no-orders-yet.png)

</details>                                                                                    

---

**Saved Addresses Management Page Screenshot:**

![User Saved Addresses Page](docs/images/screenshots/desktop-account-saved-address.png)

<details><summary>Click to View Account Empty Saved Addresses State</summary>

![Empty Saved Addresses State](docs/images/screenshots/desktop-account-no-saved-address.png)
</details>

<details><summary>Click to View Account 'Add/Edit' Address Form</summary>

![Edit Address Form](docs/images/screenshots/desktop-add-edit-address.png)

</details>

### Email Communications
- Order confirmation with license keys
- Contact form submissions
- Professional email formatting

## User Accounts And Authentication
- email or username login

**Login Page Screenshot:**
![Login Page](docs/images/screenshots/desktop-signin.png)

**Sign-up Page Screenshot:**
![Sign-up Page](docs/images/screenshots/desktop-signup.png)

**Contact Form Submission Confirmation Email:**

<img src="docs/images/screenshots/email-support.png" width="350"/>

### Informational Pages
- About Us
- FAQs
- Privacy Policy
- Terms & Conditions

**FAQS Page with Accordion Style Layout:**

![FAQS Page](docs/images/screenshots/desktop-faqs.png)

<details><summary><strong>View Privacy Policy and Terms & Conditions Screenshots</strong></summary>

**Privacy Policy Page:**
![Privacy Policy Page](docs/images/screenshots/desktop-privacy-policy.png)

**Terms & Conditions Page:**
![Terms and Conditions Page](docs/images/screenshots/desktop-terms.png)
</details>

### Customer Support
- Contact form with categorisation (dropdown options)

**Support Contact Form Screenshot:**

![Support Contact Form](docs/images/screenshots/desktop-contact-support.png)

### Admin Features
- Custom sales dashboard with analytics
- Product management interface in Django admin
- Order tracking and basic customer support tools

**Staff Only Admin Sales Analytics Dashboard:**

![Custom Admin Only Sales Analytics Dashboard](docs/images/screenshots/desktop-admin-sales-dashboard.png)

## Interactive Features

**Parallex Scrolling Effect:**
_Subtle parallax effect on about us page background image for visual engagement_

![Parallax Scrolling Effect](docs/images/screenshots/desktop-about.gif)

## Error Pages

**Custom 404 Page Screenshot:**
_Friendly message with navigation options to return to the homepage._
![404 Page Not Found](docs/images/screenshots/desktop-404.png)

**500 Server Error Page Screenshot:**
_Simple message indicating a server error occurred._

<img src="docs/images/responsiveness-screenshots/desktop-500-chrome.png" alt="500 Server Error Page" width="500"/>


## Testing

Eclipse Protocol has undergone testing to ensure security, performance, coding best practices, and user experience quality.

### Testing Overview

**Code Quality & Validation:**
- ✅ HTML5 validation (W3C Markup Validator) - all pages pass
- ✅ CSS3 validation (W3C CSS Validator) - all stylesheets pass  
- ✅ JavaScript validation (ESLint) - ES2024+ standards compliance
- ✅ Python code quality (Flake8, Black, isort) - PEP 8 compliance

**Performance & Accessibility:**
- ✅ Lighthouse testing (Performance, Accessibility, Best Practices, SEO)
- ✅ Responsive design across desktop, tablet, and mobile devices
- ✅ Cross-browser compatibility (Chrome, Firefox, Edge, Safari, Opera)
- ✅ WCAG 2.1 AA accessibility compliance

**Functional Testing:**
- ✅ User authentication and account management
- ✅ Product catalogue browsing and search functionality
- ✅ Shopping cart and wishlist operations
- ✅ Complete checkout flow with Stripe payment integration
- ✅ Digital product delivery (license keys and credits)
- ✅ Admin dashboard and product management tools
- ✅ Email notifications and customer support system

**Security & Payment Processing:**
- ✅ Stripe webhook validation and payment confirmation
- ✅ CSRF protection and form validation
- ✅ Secure handling of sensitive customer data
- ✅ Error handling and graceful failure scenarios

### Automated Testing
- **Django TestCase**: Unit and integration tests for models, views, and forms
- **Coverage.py**: Code coverage analysis with detailed reporting. _(currently at 86% coverage)_
- **Continuous Integration**: Code quality checks integrated into development workflow (manual for now, automated CI/CD planned for future)

### UK Stripe Test Cards for Development
For testing payment functionality during development, use these UK-specific test cards:

| Card Type | Number | Description |
|-----------|---------|-------------|
| UK Visa | `4000 0082 6000 0000` | UK Visa card for successful payments |
| UK Mastercard | `5555 5582 6555 4449` | UK Mastercard for successful payments |
| UK Debit Card | `4000 0582 6000 0005` | UK Debit card for successful payments |
| Declined Card | `4000 0000 0000 9995` | Simulates a declined payment |
| Insufficient Funds | `4000 0000 0000 9995` | Simulates insufficient funds scenario |

**Complete Testing Documentation:** [TESTING.md](TESTING.md)

The testing documentation includes detailed screenshots, validation results, manual test scenarios, automated test coverage reports, and browser/device compatibility testing. Known issues and limitations are also documented for transparency.

## Deployment

### Prerequisites
- Python 3.12
- Git
- GitHub account
- Heroku account
- AWS account
- Gmail account (for email functionality)

### 1. Repository Setup

#### Option A: Fork an Existing Repository
1. Navigate to the [Eclipse Protocol repository](https://github.com/Seren-Hughes/eclipse_protocol) on GitHub
2. Click the "Fork" button in the top-right corner
3. Select your account as the destination for the fork
4. Choose fork settings:
   - Keep the same repository name or change it
   - Add a description (optional)
   - Choose to copy only the main branch or all branches
5. Click "Create fork"

#### Option B: Clone Repository to Local Machine

**Method 1: Using VS Code (Recommended for Beginners)**
1. Open VS Code
2. Install GitHub extension if not already installed
3. Connect GitHub account:
   - Click Accounts icon (bottom-left)
   - Sign in to GitHub and authorise VS Code
4. Clone repository:
   - Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
   - Type "Git: Clone" and select it
   - Choose "Clone from GitHub"
   - Search and select your repository
   - Choose local folder where you want to store the project
   - Click "Open in VS Code" when cloning completes

**Method 2: Command Line (Terminal/Git Bash)**
```bash
# Navigate to where you want to store the project
cd /path/to/your/projects

# Clone the repository (replace with your actual repository URL)
git clone https://github.com/YOUR-USERNAME/eclipse-protocol-ecommerce.git

# Navigate into the project folder
cd eclipse-protocol-ecommerce

# Open in VS Code (optional)
code .
```

**Setting Up Git Configuration (First Time Only)**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

**Basic Git Workflow for Development**
```bash
# Check current status
git status

# Add changes to staging area
git add .                    # Add all changes
git add filename.py          # Add specific file

# Commit changes with descriptive message
git commit -m "Add user authentication system"

# Push changes to GitHub
git push origin main        # Push to main branch

# Pull latest changes from GitHub (before starting work)
git pull origin main
```

### 2. Local Development Setup

#### 2.1 Virtual Environment
```bash
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

#### 2.2 Environment Variables
1. Create your own `env.py` file (never commit to version control)
2. Ensure `env.py` is in your `.gitignore` (it should be already)
3. Copy the template from [env_example.py](env_example.py) and fill in your actual values - **Never commit `env.py` to version control**

**Quick Setup:**
```bash
# Copy the example file and edit with your values
cp env_example.py env.py
# Then edit env.py with your actual credentials
```

See [env_example.py](env_example.py) for the complete template with all required environment variables.

```python
import os

# Core Django
os.environ.setdefault("SECRET_KEY", "your-actual-secret-key")
os.environ.setdefault("DEBUG", "True")  # False for production

# PostgreSQL Database
os.environ.setdefault("DATABASE_URL", "your-database-url")

# Stripe Payment Processing
os.environ.setdefault("STRIPE_PUBLIC_KEY", "pk_test_your_key")
os.environ.setdefault("STRIPE_SECRET_KEY", "sk_test_your_key")
os.environ.setdefault("STRIPE_WH_SECRET", "whsec_your_webhook_secret")

# Gmail SMTP
os.environ.setdefault("EMAIL_HOST_USER", "your-store@gmail.com")
os.environ.setdefault("EMAIL_HOST_PASSWORD", "your-gmail-app-password")

# AWS S3 Storage
os.environ.setdefault("AWS_ACCESS_KEY_ID", "your-aws-access-key")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "your-aws-secret-key")
os.environ.setdefault("AWS_STORAGE_BUCKET_NAME", "your-bucket-name")

# Production Settings
os.environ.setdefault("ALLOWED_HOSTS", "localhost,127.0.0.1,your-app.herokuapp.com")
```

#### 2.3 Database Setup & Local Server
```bash
python manage.py migrate
python manage.py createsuperuser   # Create admin account
python manage.py runserver
```

#### 2.4 Code Quality & Testing Commands

**Code Formatting & Linting**
```bash
# Format Python code with Black
black .

# Sort imports with isort
isort .

# Python linting with Flake8
flake8

# Django template linting with djlint (template linting gem!)
djlint --reformat templates/
djlint --check templates/

# JavaScript linting with ESLint
npx eslint static/js/
```

**Testing & Coverage**
```bash
# Run Django tests
python manage.py test

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generates HTML coverage report in htmlcov/

# Run specific test modules
python manage.py test accounts.tests
python manage.py test cart.tests.test_views
```

**Database Management**
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Reset database (careful!)
python manage.py flush

# Load fixture data
python manage.py loaddata fixtures/sample_data.json
```

**Static Files & Media**
```bash
# Collect static files
python manage.py collectstatic

# Clear collected static files
python manage.py collectstatic --clear --noinput
```

### 3. Third-Party Services Configuration

#### 3.1 PostgreSQL Database Setup

**Getting Your Database Connection String:**
Most PostgreSQL hosting services provide a connection string in this format:
```
postgresql://username:password@host:port/database_name
```

**Common Sources:**
Neon.tech, Supabase, Heroku Postgres and DataGrip are popular options.

This project uses Neon.tech for PostgreSQL hosting (provided by Code Institute).

**Security Setup:**
1. **Never commit database URLs to version control**
2. Store in `env.py` for local development:
   ```python
   os.environ.setdefault("DATABASE_URL", "postgresql://your-connection-string-here")
   ```
3. Add to Heroku Config Vars for production deployment

**Verify Connection:**
```bash
# Test local connection
python manage.py migrate
python manage.py dbshell  # Opens database shell if connection works
```

**Important:** Your database URL contains sensitive credentials. Always store it as an environment variable, never in your code.

#### 3.2 AWS S3 Setup for Media Storage

**3.2.1 Create S3 Bucket**
1. AWS Console → S3 → Create bucket
2. Enter unique bucket name (e.g., `your-project-name-media`)
3. **Select region** (choose closest to your target users - e.g., `US East (N. Virginia) us-east-1` for general use, `EU West (London) eu-west-2` for UK/EU) _This project uses eu-west-2_.
4. Configure settings as needed → Create bucket

**3.2.2 Configure Bucket Permissions**

**Bucket Policy** (replace `YOUR-BUCKET-NAME`):
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
    }
  ]
}
```

**CORS Configuration:**
For this Django + S3 setup, CORS configuration is not currently required since static files are served directly by the browser. If the site loads images and static files correctly, the CORS configuration can be left empty.

*CORS is only needed if JavaScript AJAX requests directly to the S3 bucket from the frontend.*

**3.2.3 Create IAM User**
1. IAM → Users → Create user (e.g., `eclipse-protocol-s3-user`) → Select "Programmatic access"
2. Attach policies: `AmazonS3FullAccess`
3. **Important**: Save Access Key ID and Secret Access Key securely

#### 3.3 Stripe Payment Integration

**3.3.1 Get API Keys**
1. Create Stripe account and access Dashboard
2. Navigate to "Developers" → "API keys"
3. Obtain your keys:
   - **Publishable key** (`pk_test_` for development, `pk_live_` for production)
   - **Secret key** (`sk_test_` for development, `sk_live_` for production)

**3.3.2 Configure Webhook Endpoint**
1. In Stripe Dashboard, go to "Developers" → "Webhooks"
2. Click "Add endpoint"
3. Enter endpoint URL: `https://your-app-name.herokuapp.com/checkout/webhook/`
4. Select events to listen for:
   - `payment_intent.succeeded` - When payment completes successfully
   - `payment_intent.payment_failed` - When payment fails or is declined
5. Click "Add endpoint"
6. Copy the **Webhook signing secret** (`whsec_...`) - this verifies webhook authenticity

**Why Webhooks Matter:**
Webhooks ensure your application receives reliable payment confirmation even if the customer closes their browser or loses internet connection during checkout. The webhook handling creates orders, generates license keys, and sends confirmation emails.

**Testing Webhooks Locally:**
For local development, use Stripe CLI to forward webhooks:
```bash
# Install Stripe CLI, then:
stripe login
stripe listen --forward-to localhost:8000/checkout/webhook/
```

#### 3.4 Gmail SMTP Configuration
1. Create dedicated Gmail account for transactional emails
2. Enable 2-factor authentication
3. Generate App Password (Google Account Settings → Security → App passwords)
4. Use 16-character app password for `EMAIL_HOST_PASSWORD`

**Email Customisation:**
This project automatically configures emails to display as "Eclipse Protocol" instead of just the plain email address. This is handled in `settings.py`:
```python
DEFAULT_FROM_EMAIL = f"Eclipse Protocol <{EMAIL_HOST_USER}>"
```
No additional environment variables needed - this uses the existing `EMAIL_HOST_USER`.

### 4. Heroku Deployment & Hosting

**Important**: Heroku Eco dynos "sleep" after 30 minutes of inactivity and require 10-15 seconds to "wake up" on first access. This is normal behaviour for free/low-cost hosting tiers and does not reflect the application's actual performance once active.

#### 4.1 Required Files
Ensure these files exist in your project root:
- **requirements.txt** - Python dependencies (already included)
- **Procfile** containing:
  ```
  web: gunicorn eclipse_protocol.wsgi
  ```
- **runtime.txt** containing:
  ```
  python-3.12
  ```

#### 4.2 Heroku Account Setup
1. Create account at [heroku.com](https://heroku.com)
2. Verify email address
3. Complete account setup

#### 4.3 Deploy via Heroku Dashboard (Recommended)

**Create Heroku App:**
1. Log into [Heroku Dashboard](https://dashboard.heroku.com)
2. Click "New" → "Create new app"
3. Enter app details:
   - App name: Must be unique (e.g., `eclipse-protocol-your-name`)
   - Region: Choose closest to your users (US/Europe)
4. Click "Create app"

**Connect GitHub Repository:**
1. Go to "Deploy" tab in your Heroku app dashboard
2. Deployment method section: Click "GitHub"
3. Connect to GitHub:
   - Click "Connect to GitHub"
   - Authorise Heroku to access your GitHub account
4. Search for repository:
   - Enter your repository name
   - Click "Search"
   - Click "Connect" next to your repository

**Configure Automatic Deployments (Optional but Recommended):**
1. In "Automatic deploys" section:
   - Select branch: Usually `main`
   - Check "Wait for CI to pass before deploy" (if using CI)
   - Click "Enable Automatic Deploys"

*What this means: Every time you push to GitHub, Heroku automatically updates your live site*

**Important Considerations:**
- Testing recommended: Set up automated tests to ensure code quality before automatic deployment
- Security: Always use environment variables for sensitive data
- Branch protection: Consider enabling branch protection rules on GitHub for additional safety

**Set Environment Variables via Heroku Dashboard:**
1. Go to "Settings" tab in your Heroku app
2. Click "Reveal Config Vars"
3. Add each environment variable as key-value pairs:

| Key | Value Example | Notes |
|-----|---------------|-------|
| `SECRET_KEY` | `your-django-secret-key` | Generate new for production |
| `DEBUG` | `False` | **Always False in production!** |
| `DATABASE_URL` | `postgresql://...` | From Code Institute (Neon database) |
| `AWS_ACCESS_KEY_ID` | `AKIA...` | From IAM user creation |
| `AWS_SECRET_ACCESS_KEY` | `your-secret-key` | From IAM user creation |
| `AWS_STORAGE_BUCKET_NAME` | `your-bucket-name` | Your S3 bucket name |
| `AWS_REGION` | `eu-west-2` | Your S3 bucket region |
| `STRIPE_PUBLIC_KEY` | `pk_test_...` or `pk_live_...` | From Stripe dashboard |
| `STRIPE_SECRET_KEY` | `sk_test_...` or `sk_live_...` | From Stripe dashboard |
| `STRIPE_WH_SECRET` | `whsec_...` | Webhook signing secret |
| `EMAIL_HOST_USER` | `your-store@gmail.com` | Gmail account |
| `EMAIL_HOST_PASSWORD` | `16-char-app-password` | Gmail app password |
| `SITE_URL` | `https://your-app-name.herokuapp.com/` | Your live site URL (include trailing slash)  |
| `ALLOWED_HOSTS` | `your-app-name.herokuapp.com` | Your Heroku domain |

4. Click "Add" after entering each key-value pair

**Manual Deploy:**
1. In "Manual deploy" section:
   - Select branch to deploy (usually `main`)
   - Click "Deploy Branch"
   - Wait for build to complete (you'll see build logs)
   - Click "View" to see your live app

#### 4.4 Deploy via Heroku CLI (Alternative Method)

**Create and Deploy:**
```bash
heroku login
heroku create your-app-name
```

**Set Config Vars:**
```bash
# Django
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False
heroku config:set DATABASE_URL="your-database-url"

# AWS
heroku config:set AWS_ACCESS_KEY_ID="your-aws-access-key"
heroku config:set AWS_SECRET_ACCESS_KEY="your-aws-secret-key"
heroku config:set AWS_STORAGE_BUCKET_NAME="your-bucket-name"
heroku config:set AWS_REGION="your-bucket-region"

# Stripe
heroku config:set STRIPE_PUBLIC_KEY="pk_test_your_key"
heroku config:set STRIPE_SECRET_KEY="sk_test_your_key"
heroku config:set STRIPE_WH_SECRET="whsec_your_secret"

# Email
heroku config:set EMAIL_HOST_USER="your-gmail-address"
heroku config:set EMAIL_HOST_PASSWORD="your-gmail-app-password"

# Site Configuration
heroku config:set SITE_URL="https://your-app-name.herokuapp.com/"

# Security
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
```

**Release & Setup:**
```bash
git push heroku main

# Via Heroku CLI
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
heroku run python manage.py createsuperuser
```

#### 4.5 Post-Deployment Setup
Run these commands via Heroku CLI or Dashboard Console:

**Via Heroku Dashboard Console:**
1. Go to "More" → "Run console"
2. Enter each command:
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py createsuperuser
   ```

### 5. Post-Deployment Verification

#### 5.1 Test Core Functionality Checklist
- [ ] Site loads without errors
- [ ] User registration and login
- [ ] Product browsing and details
- [ ] Add to cart functionality
- [ ] Checkout process (use Stripe test cards)
- [ ] Order confirmation emails
- [ ] Admin panel access
- [ ] Static files and images display correctly

#### 5.2 Stripe Test Cards
Use these test cards for payment testing:

| Card Number | Description | Region |
|-------------|-------------|---------|
| `4242424242424242` | Successful payment | International |
| `4000000000000002` | Declined payment | International |
| `4000000000009995` | Insufficient funds | International |
| `4000008260000000` | UK Visa | United Kingdom |
| `4000058260000005` | UK Visa (debit) | United Kingdom |
| `5555558265554449` | UK Mastercard | United Kingdom |

Use any future expiry date and any 3-digit CVC.

### 6. Ongoing Development Workflow

1. **Make changes locally**
2. **Test thoroughly** with `python manage.py runserver`
3. **Run code quality checks:**
   ```bash
   black .
   isort .
   flake8
   djlint --check templates/
   python manage.py test
   ```
4. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```
5. **Deploy to Heroku:**
   - If automatic deploys enabled: Heroku automatically updates
   - If manual deploy needed: Go to Heroku dashboard → Deploy tab → "Deploy Branch"

### 7. Useful Development Commands

#### 7.1 Code Quality & Testing
```bash
# Complete code quality check
black . && isort . && flake8 && djlint --check templates/

# Run tests with coverage report
coverage run --source='.' manage.py test && coverage report

# Generate HTML coverage report
coverage html

# Check template formatting
djlint templates/ --profile=django

# Reformat templates
djlint templates/ --reformat --profile=django
```

#### 7.2 Heroku CLI Commands
```bash
# View recent logs
heroku logs --tail -a your-app-name

# Run Django management commands
heroku run python manage.py migrate -a your-app-name
heroku run python manage.py createsuperuser -a your-app-name

# Access Django shell
heroku run python manage.py shell -a your-app-name

# View config variables
heroku config -a your-app-name

# Restart application
heroku restart -a your-app-name
```

### 8. Troubleshooting

#### Common Issues

**Application Won't Start:**
```bash
# View logs to identify the issue
heroku logs --tail -a your-app-name

# Check configuration
heroku config -a your-app-name
```

**Static Files Not Loading:**
- Verify AWS S3 bucket policy allows public read access
- Check AWS credentials in Heroku config vars
- Run `python manage.py collectstatic` after deployment

**Payment Issues:**
- Verify Stripe keys are correctly set in Heroku config vars
- Check webhook endpoint URL matches your live domain
- Ensure webhook signing secret is correct

**Email Not Sending:**
- Verify Gmail app password is correct (not your regular password)
- Check Gmail account has 2FA enabled
- Confirm `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` in config vars

#### Database Issues
```bash
# Reset database (careful!)
heroku run python manage.py flush -a your-app-name

# Check migration status
heroku run python manage.py showmigrations -a your-app-name

# Apply specific migration
heroku run python manage.py migrate app_name migration_name -a your-app-name
```

### 9. Security Checklist

- [ ] `DEBUG = False` in production
- [ ] All sensitive keys stored in Heroku Config Vars
- [ ] `env.py` listed in `.gitignore` and never committed
- [ ] Strong, unique `SECRET_KEY` for production
- [ ] HTTPS enforced (automatic on Heroku)
- [ ] Stripe webhook endpoints secured with signing secret
- [ ] Database credentials managed securely
- [ ] AWS S3 bucket properly configured with public read access only

---

**Live Application**: [Eclipse Protocol E-Commerce Store](https://eclipse-protocol-15d26c9e2a55.herokuapp.com/)

*Note: Heroku eco dynos may require 10-15 seconds to wake up after periods of inactivity.*

## Credits & References

### Images 

All product images sourced from Adobe Stock with appropriate licenses for use in this project.

- [Illustration of an astronaut in space battlefield](https://stock.adobe.com/uk/images/illustration-of-an-astronaut-in-space-battlefield-idea-for-sci-fi-and-space-punk-background-wallpaper-generative-ai/572940289?prev_url=detail) - Used for Store Hero Banner

- [Illustration of an astronaut in space battlefield](https://stock.adobe.com/uk/images/illustration-of-an-astronaut-in-space-battlefield-idea-for-sci-fi-and-space-punk-background-wallpaper-generative-ai/573799817?prev_url=detail) - Used for Base Game Product Standard Edition

- [Game characters action scene](https://stock.adobe.com/uk/images/game-characters-action-scene-with-soldiers-in-armor-at-war-against-invading-monsters-and-aliens-science-fiction-epic-battle-high-tech-ai-generated-image/607116700?prev_url=detail) - Used for Game Product Ultimate Edition

- [Colorful glowing cards with space themes](https://stock.adobe.com/uk/images/colorful-glowing-cards-with-space-themes-stacked-on-a-wooden-surface-showcasing-vibrant-cosmic-designs-and-swirling-patterns-during-a-dimly-lit-evening/1084682717?prev_url=detail) - Used for Currency Pack Product Images

- [Neon lit futuristic playing cards on reflective surface](https://stock.adobe.com/uk/images/neon-lit-futuristic-playing-cards-on-reflective-surface/1313932597?prev_url=detail) - Used for Currency Pack Product Images

- [Landscape image of Llyn Idwal and Twll Du in Eryri - Snowdonia](https://stock.adobe.com/uk/images/digital-composite-milky-way-image-of-beautiful-landscape-image-of-llyn-idwal-and-devil-s-kitchen-in-snowdoina/244159042?prev_url=detail) - Used for About Us Page Background 

- [Responsive display banner](https://ui.dev/amiresponsive) - Used for the banner image in README.md

### Icons

- [Font Awesome](https://fontawesome.com/) - All icons used throughout the site including the astronaut used in brand logo and favicon.

### Fonts

Fonts sourced from Google Fonts:

- Arimo - designed by Steve Matteson

- Oswald - designed by Vernon Adams, Kalapi Gajjar, Cyreal

### References

**Documentation & Official Resources:**
- [Django 5.2 Documentation](https://docs.djangoproject.com/en/5.2/) - Framework implementation, models, views, forms, and authentication
- [Stripe Developer Documentation](https://docs.stripe.com/) - Payment processing, webhooks, and testing
- [Stripe Testing Guide (UK locale)](https://docs.stripe.com/testing?locale=en-GB) - Payment testing and card numbers
- [Stripe Declined Payments Testing](https://docs.stripe.com/testing?locale=en-GB&testing-method=card-numbers#declined-payments) - Error handling scenarios
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/) - Cloud storage setup and configuration
- [Heroku Dev Center](https://devcenter.heroku.com/) - Deployment and configuration guides
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/getting-started/contents/) - Responsive design and components


**Code Quality & Testing Resources:**
- [Django Testing Documentation](https://docs.djangoproject.com/en/5.2/topics/testing/) - Unit testing and test coverage
- [Black Code Formatter](https://black.readthedocs.io/) - Python code formatting standards
- [Flake8 Documentation](https://flake8.pycqa.org/) - Python linting and style guide enforcement
- [Coverage.py Documentation](https://coverage.readthedocs.io/) - Code coverage analysis and reporting

**Technical Implementation Guides:**
- [Django Context Processors Documentation](https://docs.djangoproject.com/en/5.2/ref/templates/api/#writing-your-own-context-processors) - Custom template context implementation
- [Django Signals Documentation](https://docs.djangoproject.com/en/5.2/topics/signals/) - Automated license key generation
- [Writing Custom Django Admin](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/) - Admin interface customization
- [Django Email Backend Configuration](https://docs.djangoproject.com/en/5.2/topics/email/) - SMTP setup and email delivery
- [Django Static Files in Production](https://docs.djangoproject.com/en/5.2/howto/static-files/deployment/) - AWS S3 integration

**E-commerce & Payment Processing:**
- [Wise - Stripe Test Cards Guide](https://wise.com/gb/blog/stripe-payments-test-cards) - UK-specific payment testing
- [Code Institute Boutique Ado Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1) - E-commerce functionality reference and Django implementation patterns
- [MailerLite Responsive Email Design Guide](https://www.mailerlite.com/blog/guide-to-responsive-email-design) - Transactional email templates and formatting

**Web Standards & Accessibility:**
- [MDN Web Docs](https://developer.mozilla.org/) - HTML5, CSS3, and JavaScript implementation
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Accessibility compliance and testing
- [W3C HTML Validator](https://validator.w3.org/) - Markup validation
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Stylesheet validation

**Design & UX Resources:**
- [Google Fonts](https://fonts.google.com/) - Typography selection (Arimo, Oswald)
- [Font Awesome](https://fontawesome.com/) - Icon library and implementation
- [Coolors](https://coolors.co/) - Colour palette generation and accessibility testing
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) - Colour accessibility validation
- [Shields.io](https://shields.io/) - README badge generation

**Development Tools & Workflow:**
- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects) - Agile project management and issue tracking
- [Git Documentation](https://git-scm.com/doc) - Version control workflows and best practices
- [VS Code Documentation](https://code.visualstudio.com/docs) - Development environment setup and extensions

**Community Resources & Problem Solving:**
- [Stack Overflow](https://stackoverflow.com/) - Technical problem solving and Django community support
- [Django Community Forums](https://forum.djangoproject.com/) - Framework-specific discussions and troubleshooting
- [Code Institute Community](https://codeinstitute.net/) - Peer support  throughout development
- [MDN Learning Area](https://developer.mozilla.org/en-US/docs/Learn) - Web development fundamentals and best practices

**Legal & Compliance:**
- [TermsFeed Privacy Policy Generator](https://www.termsfeed.com/privacy-policy-generator/) - Privacy policy creation
- [TermsFeed Terms & Conditions Generator](https://app.termsfeed.com/wizard/terms-conditions) - Terms of service creation


## Acknowledgements:

**Daniel Hamilton - Code Institute Mentor**

Special thanks to Daniel for his exceptional guidance throughout the Full Stack Web Development Diploma. His insightful feedback, practical advice, and clear explanations across all projects have been invaluable to my development as a programmer and the successful completion of this final project.

**Marko Tot - Code Institute Facilitator** 
I'm grateful to Marko for his dedicated support throughout the course. The resources he shared with our cohort and the collaborative learning environment he fostered significantly enhanced my learning experience and enjoyment of the programme.

**My Family & Husband**
Thank you to my family and my husband for their unwavering patience and encouragement during the intensive final stages of this project. Their understanding during countless evenings of debugging and development work made all the difference. Special appreciation to my dad for his valuable time testing the checkout process and providing thoughtful usability feedback that helped improve the user experience.

**Code Institute Community**
Thanks to my fellow students and the wider Code Institute community for the shared learning, discussions, and problem-solving along the way.