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
3. [Project Management & Planning](#project-management--planning)
4. [User Stories by Theme and Epic](#user-stories-by-theme-and-epic)
5. [Effort Risk Fibonacci Matrix](#effort-risk-fibonacci-matrix)
6. [ERD Diagram](#erd-diagram)
7. [Site Map](#site-map)
8. [User Flow Diagrams](#user-flow-diagrams)
9. [Products & Catalogue Structure](#products--catalogue-structure)


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

## ERD Diagram:

![Eclipse Protocol E-Commerce ERD](docs/images/diagrams/eclipse-protocol-erd.png)

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
| 10,000 | £69.99 |

For this portfolio project, this is simulated - the credits are "delivered" instantly and visible in order history. (Balance managed in‑game - no API integration implemented).

#### 2. Base Game (License Keys)

Sold in platform-specific editions, each with its own license key.

| Edition | Price | Platforms |
|---------|-------|-----------|
| Standard | £49.99 | PC (Steam), Xbox, Nintendo |
| Premium | £59.99 | PC (Steam), Xbox, Nintendo |
| Ultimate | £69.99 | PC (Steam), Xbox, Nintendo |

**PlayStation:** _Links externally to the official PlayStation Store for realism as PlayStation does not support third-party license key sales._

**MVP Approach:** Only the Standard Edition will be included for MVP - each platform version is stored as a separate product (unique SKU and license key).

**License Delivery:** The license key is shown in the user dashboard and emailed after checkout.

**Base Game Licence Keys** Implementation Details:
When a player purchases a game edition, the system generates a unique licence key using either a UUID/ULID pattern.
The key is stored in the license_keys table, linked to the specific order item and user, and is displayed in the user’s account as well as included in the confirmation email.

_**Note:** For this project, keys are generated on demand rather than managed as a pre-generated inventory pool, which keeps the implementation simple while still simulating a realistic digital delivery flow._

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
