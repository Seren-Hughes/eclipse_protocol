# Eclipse Protocol E-Commerce 

A fictional e-commerce platform for a speculative video game company, Dark Sky Games, selling digital products and physical merchandise on a dedicated store for their game - Eclipse Protocol. 

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