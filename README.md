# Eclipse Protocol E-Commerce 

A fictional e-commerce platform for a speculative video game company, Dark Sky Games, selling digital products and physical merchandise on a dedicated store for their game - Eclipse Protocol. 

## Project Purpose & Value Proposition

The in-game currency system for Eclipse Protocol is inspired by established models used in games such as Roblox (Robux) and Apex Legends (Apex Coins) by EA Games.
Virtual currencies have become a standard part of modern game economies, offering a consistent way to handle microtransactions, cosmetic content, and bundled purchases across platforms and regions.
Adopting a credit-based system in this project helps to replicate a realistic e-commerce flow while reflecting common monetisation structures found in contemporary digital game stores.

**Purpose:** To create a secure, user-friendly e-commerce platform that enables customers to purchase digital game content (license keys, in-game currency, DLC) and physical merchandise, while providing administrators with comprehensive tools to manage products, orders, and customer relationships.

**Value to Users:**
- **Customers** can conveniently purchase and instantly access digital game content through a single platform, with their purchase history and license keys stored securely in their account dashboard
- **Site Administrators** gain management tools through Django's admin interface to handle product catalogues, process orders, manage license key inventory, and moderate user-generated content
- **Business Owner** benefits from a scalable platform that can grow from digital-only sales to include subscriptions, physical merchandise, and community features

**Technical Implementation:** This project showcases full-stack development skills including Django backend architecture, PostgreSQL relational database design, Stripe payment integration, responsive frontend design with Bootstrap, and deployment to a production environment. The MVP focuses on core e-commerce functionality with digital product delivery, while the modular structure allows for future expansion into subscriptions, physical goods fulfillment, and advanced analytics.


# Contents:
- [Wireframes](#wireframes)
- [Colour Palette](#colour-palette)
- [Project Management & Planning](#project-management--planning)
- [User Stories by Theme and Epic](#user-stories-by-theme-and-epic)
- [Effort Risk Fibonacci Matrix](#effort-risk-fibonacci-matrix)
- [ERD Diagram](#erd-diagram)
- [Site Map](#site-map)
- [User Flow Diagrams](#user-flow-diagrams)
- [Products & Catalogue Structure](#products--catalogue-structure)
- [JavaScript Enhancements](#javascript-enhancements)

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

## Project management & Planning:

This project was planned and managed using agile methodology, utilising GitHub projects and Miro whiteboards.  

### Agile Approach & Story Points

User stories are estimated using **Fibonacci sequence story points** (1, 2, 3, 5, 8, 13) to reflect the relative effort, complexity, and uncertainty of each task. Story points consider:
- Development time
- Technical complexity
- Dependencies on other features
- Testing requirements

**Total Project Scope:** 31 user stories across 9 themes and 15 epics, totaling **145 story points**.

**MVP Scope:** Focus on **Must Have** features to deliver a functional e-commerce platform:
- **16 Must Have stories = 85 points**
- Core digital storefront functionality
- Secure checkout and payment processing
- User authentication and account management
- Admin product and order management

**MoSCoW Prioritization Breakdown:**
- **Must Have:** 16 stories (85 points) - MVP core functionality
- **Should Have:** 9 stories (44 points) - Phase 2 enhancements
- **Could Have:** 8 stories (31 points) - Phase 3 value-adding features
- **Won't Have:** 2 stories (10 points) - Future consideration

### Scalability & Future Iterations

The epic-based structure allows for flexible expansion as the business evolves. After MVP delivery, subsequent sprints can address Should Have and Could Have features based on:
- **Customer feedback** - Prioritize features users request most
- **Business metrics** - Add functionality that drives conversions
- **Technical capacity** - Balance new features with technical debt
- **Market changes** - Adapt to emerging e-commerce trends

## User Stories by Theme and Epic:

### Theme 1: Digital Storefront
#### Epic 1.1: Browse & Discover Digital Products
|Story No. |User Story |Story Points |Priority |
|-------------------|------------------------|----|--------------|
| 1.1.1	 | As a customer, I want to browse all available digital products (base game, DLC, credits) so I can see what's available for my platform. |	5 |	Must Have |
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
| 2.4.1	 | As a site admin, I want to manage license key generation and mark keys as redeemed so availability stays accurate. |	5 |	Could Have |

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

The database for Eclipse Protocol is designed around a digital-first e-commerce flow, with support for user accounts, digital products, credit packs, orders, and future extensions such as subscriptions and physical merchandise.

#### Users & Profiles

`users`
Stores core authentication details (email, password, username, flags for staff/superuser, timestamps).
This is aligned with Django’s built-in user model and is responsible for login, registration, and access control.

`user_profiles`
Extends the user model with additional information such as first name, last name, phone number, and a reference to the user’s default address.
This keeps authentication concerns separate from profile data.

`addresses`
Holds billing and shipping addresses linked to a user.
Each address has fields such as full name, street, city, postcode, country, and an address_type (e.g. billing or shipping).
At checkout, a snapshot of the chosen address is copied onto the orders table so that order history remains accurate even if the user later updates their profile.

#### Products & Catalogue

`products`
Central catalogue table for all products sold in the store (base game editions, credit packs, physical items, and future subscriptions).
Includes fields such as name, slug, description, price, product_type (e.g. base_game, currency, physical, subscription), SKU, image, active flag, and timestamps.
The product_type field is used to drive filtering and UI behaviour (e.g. separating digital products from merchandise).

`digital_products`
Stores additional details for digital game products.
Each row is linked to a product and includes platform (PC, Xbox, Nintendo, etc.), edition (Standard, Premium, Ultimate), and flags indicating whether the product is a base game edition and whether it requires a licence key.
This allows the store to treat platform/edition combinations as distinct SKUs while still sharing core product information.

`currency_products`
Represents in-game currency packs (e.g. 100, 500, 1,200 credits).
Each currency product is linked to a product row and includes a credit_amount.
The e-commerce system records the purchase of these packs; in a real game integration the actual in-game balance would be managed by the game backend.

`physical_products` (future / Could Have)
Stores extra metadata for physical merchandise items such as weight, size options, colour options, and stock levels.
Note: for apparel (e.g. hoodies in sizes XS–XL), a real production system would typically introduce a separate product_variants table with variant-level SKUs for each size/colour combination (e.g. one SKU per size and colour). This level of complexity is outside the scope of the MVP but is acknowledged as a necessary extension for a full merchandise implementation.

#### Cart, Wishlist & Checkout

`cart_items`
Stores items that a user has added to their shopping cart.
Each row links a user (or optional session ID), product, quantity, and timestamps.
A uniqueness constraint on (user_id, product_id) ensures each product appears only once per user’s cart.

`wishlists`
Allows logged-in users to save products for later.
Each row connects a user to a product, with a unique pair per user/product combination.

#### Orders, Order Items & Payments

`orders`
Represents a completed or in-progress order.
Stores an order_number, reference to the user, a snapshot of billing/shipping details (name, address, email), pricing fields (order_total, delivery_cost, grand_total), Stripe PaymentIntent ID, and a consolidated status (e.g. pending, paid, refunded).

_**Note on Address Snapshots:**_ At checkout, a snapshot of the chosen address is copied onto the orders table so that order history remains accurate even if the user later updates their profile. Orders also keep nullable pointers to the user’s saved addresses for convenience in the UI. If a user edits or deletes a saved address later, the order snapshot remains unchanged. If a saved address is deleted, the order’s address pointer is set to NULL; the snapshot fields still display correctly.

Why:
- Prevents historical drift (old orders “changing” when a user updates addresses)
- Keeps invoices and email receipts consistent over time
- Still allows quick navigation from an order to the user’s current saved address when it exists

`order_items`
Stores individual line items within an order.
Each item is linked to an order and a product and records the product name, optional SKU, quantity, unit price at the time of purchase, and line total.
This ensures order histories remain accurate even if product data changes later.

`payments`  
Tracks payment transactions associated with an order.
Includes Stripe PaymentIntent ID, amount, currency, status (e.g. succeeded, pending, failed), and optional refund details.
This table provides a clear audit trail for payment flows.

#### Digital Delivery (Licence Keys)

`license_keys`
Handles digital delivery for base game editions that require a key.
Each row links to a product, an order_item, and a user, and stores a unique key_code (generated via UUID/ULID when the order is paid), the target platform, and timestamps.
Keys are generated on demand for each purchase and are shown in the user’s account and sent via email, simulating a realistic digital redemption flow without the complexity of managing a pre-generated key inventory pool.

#### Marketing & Subscriptions

`newsletter_subscriptions`
Stores newsletter sign-ups, with support for both registered users and guest emails.
Tracks whether the subscription is active and the timestamps for subscribe/unsubscribe events.

`subscription_plans` (future / Phase 2)
Defines potential Eclipse+ subscription plans (e.g. monthly or annual), linked back to the products table.
For the MVP, subscriptions are treated as a planned enhancement rather than fully implemented functionality.

## Site Map:

```
Home Page
│
├── Products
│   ├── All Products
│   ├── Search Results
│   ├── Digital Products
│   │   ├── Base Game
│   │   │   └── Edition Details
│   │   ├── DLC
│   │   └── Game Currency
│   └── Merchandise
│       └── Merchandise Detail
│
├── Eclipse+ Subscription (Public view, purchase requires login)
│    └── Subscription Payment Page
│      └── Subscription Confirmation
│
├── Shopping Cart (Public - view only)
│
├── Authentication
│   ├── Login
│   └── Sign-up
│       │
│       └── (After login) →
│           │
│           ├── Account Dashboard
│           │   ├── Profile Details
│           │   ├── Order History
│           │   ├── Saved Addresses
│           │   ├── Manage Subscription
│           │   └── Account Settings
│           │
│           ├── Wishlist (Login Required)
│           │
│           └── Checkout (Login Required)
│               ├── Billing Details
│               ├── Shipping Method (if physical items)
│               ├── Review Order
│               ├── Payment Method
│               └── Order Confirmation
│
├── Support/Help Center (Public)
│   ├── Contact/Support Form
│   └── Submission Confirmation
│   
│
├── Information Pages (Public)
│   └── Single page with accordion/expandable sections:
│       ├── About Us
│       ├── FAQs
│       ├── Terms & Conditions
│       ├── Privacy Policy
│       ├── Returns & Refunds
│       └── Shipping Information
│
├── Django Admin Panel (Staff Only)
│   ├── User Management
│   ├── Refund Management
│   ├── Product Management
│   ├── Order Management
│   ├── Review Moderation
│   ├── Newsletter Subscribers
│   └── License Key Management*
│`
└── Footer
    ├── Social Media Links
    ├── About Us (quick link)
    ├── Newsletter Signup
    ├── FAQs (quick link)
    ├── Terms & Conditions (quick link)
    ├── Privacy Policy (quick link)
    ├── My Account (quick link)
    └── Contact Us


```
**Authentication Notes:**
- Product browsing is public to encourage discovery
- Cart viewing is public, but checkout requires login
- Digital content purchases require logged-in account (must match game platform credentials for in-game currency/credit/dlc delivery)
- Wishlist access requires login - guests redirected to sign-in page with return URL
- Account dashboard and order history are only accessible to logged-in users

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
| Premium | £69.99 | PC (Steam), Xbox, Nintendo |
| Ultimate | £89.99 | PC (Steam), Xbox, Nintendo |

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
| 6 × Credit Packs | Simple to implement, instant digital delivery |
| 3 × Standard Edition Platforms (PC, Xbox, Nintendo) | Demonstrates license-key purchase and platform variation |
| License-Key Generation + Email Delivery | Required to show purchase confirmation and digital fulfilment |

**Total MVP Products: ~9 SKUs** (6 credit packs + 3 platform editions)

The MVP includes a total of 9 distinct digital products (6 currency packs and 3 platform editions of the base game). This demonstrates the full range of product catalogue, filtering, checkout, and digital delivery features.

---

### Later Phases

| Phase | Additions |
|-------|-----------|
| Phase 2 (Should Have) | Premium & Ultimate Editions, Eclipse+ Subscriptions, Refund system |
| Phase 3 (Could Have) | Physical merch, DLC packs |


### JavaScript Enhancements

To enhance user experience, custom JavaScript will be implemented for:

- **Dynamic Cart Management:** Add/remove items and update quantities without page reload (using AJAX)
- **Platform Filtering:** Real-time product filtering by platform compatibility
- **Form Validation:** Client-side validation with visual feedback before submission
- **Wishlist Toggle:** Instant wishlist add/remove with visual confirmation
- **Accordion Interactions:** Smooth expand/collapse for information sections
- **Quantity Selectors:** Interactive +/- buttons for product quantities
- **Toast Notifications:** Non-intrusive success/error messages for user actions

These features improve responsiveness and reduce page reloads, creating a more fluid shopping experience.