# StoreManager REST API Specification

Link : https://builehongtam.id.vn/DBMS/api/

---

## 1. Security & Identity (Auth)
Handles customer authentication workflows, account registration, token rotation, and self-profile queries.

| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/auth/login` | `None` | `None` | `LoginRequest` | Public (Guest) |
| **POST** | `/auth/register` | `None` | `None` | `RegisterRequest` | Public (Guest) |
| **POST** | `/auth/logout` | `None` | `allDevices` | `Optional LogoutRequest` | Authenticated User |
| **POST** | `/auth/refresh-token` | `None` | `None` | `RefreshTokenRequest` | Public (Guest) |
| **GET** | `/users/me` | `None` | `includeStore, includeRole` | `None` | Authenticated User |

---

## 2. Analytics Dashboard
Provides high-level sales metrics, conversion performance matrices, and currency-adjusted revenue summaries.

| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/overview/summary` | `None` | `from, to, timezone, currency` | `None` | System Administrator |

---

## 3. Shop Configuration
Configures merchant shop settings, metadata overrides, and brand logo asset uploads.

| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/store` | `None` | `includeOwner, includeSettings` | `None` | System Administrator |
| **PUT** | `/store` | `None` | `None` | `UpdateStoreRequest` | System Administrator |
| **POST** | `/store/logo` | `None` | `replaceExisting` | `multipart/form-data` | System Administrator |

---

## 4. Product Inventory
Handles inventory catalogs, pricing structures, category filters, and product image uploads.

| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/products` | `None` | `search, status, type, categoryId, minPrice, maxPrice, stockStatus, createdFrom, createdTo, sort, page, pageSize` | `None` | Public (Guest) |
| **GET** | `/products/{productId}` | `productId` | `includeImages, includeVariants, includeStatistics` | `None` | Public (Guest) |
| **POST** | `/products` | `None` | `publishImmediately` | `CreateProductRequest` | System Administrator |
| **PUT** | `/products/{productId}` | `productId` | `None` | `UpdateProductRequest` | System Administrator |
| **DELETE** | `/products/{productId}` | `productId` | `force, deleteAssets` | `None` | System Administrator |
| **POST** | `/products/{productId}/images` | `productId` | `setAsPrimary, position` | `multipart/form-data` | System Administrator |

---

## 5. Order Management
Coordinates purchase invoice operations, shipment tracking, billing states, and status updates.

| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/orders` | `None` | `search, customerId, status, paymentStatus, fulfillmentStatus, createdFrom, createdTo, minTotal, maxTotal, sort, page, pageSize` | `None` | Administrator / User |
| **GET** | `/orders/{orderId}` | `orderId` | `includeItems, includeCustomer, includePayments, includeHistory` | `None` | Administrator / User |
| **POST** | `/orders` | `None` | `None` | `CreateOrderRequest` | Administrator / User |
| **PUT** | `/orders/{orderId}` | `orderId` | `None` | `UpdateOrderRequest` | System Administrator |
| **PATCH** | `/orders/{orderId}/status` | `orderId` | `notifyCustomer` | `UpdateOrderStatusRequest` | System Administrator |
| **DELETE** | `/orders/{orderId}` | `orderId` | `None` | `None` | System Administrator |

---

## 6. Accounts & Customers
Administers customer account profiles, bulk data export, and customer member hierarchies.

### Main Customer Records
| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/customers` | `None` | `search, status, category, memberType, createdFrom, createdTo, lastActiveFrom, lastActiveTo, sort, page, pageSize` | `None` | System Administrator |
| **GET** | `/customers/summary` | `None` | `from, to, timezone` | `None` | System Administrator |
| **GET** | `/customers/export` | `None` | `search, status, category, memberType, createdFrom, createdTo, lastActiveFrom, lastActiveTo, format` | `None` | System Administrator |
| **GET** | `/customers/{customerId}` | `customerId` | `includeUsers, includeStatistics, includeMetadata` | `None` | System Administrator |
| **POST** | `/customers` | `None` | `sendInvitation` | `CreateCustomerRequest` | System Administrator |
| **PUT** | `/customers/{customerId}` | `customerId` | `None` | `UpdateCustomerRequest` | System Administrator |
| **DELETE** | `/customers/{customerId}` | `customerId` | `force, anonymizeData` | `None` | System Administrator |
| **POST** | `/customers/{customerId}/logo` | `customerId` | `replaceExisting` | `multipart/form-data` | System Administrator |
| **GET** | `/customers/{customerId}/orders` | `customerId` | `status, paymentStatus, createdFrom, createdTo, sort, page, pageSize` | `None` | System Administrator |

### Customer Staff & Sub-users
| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/customers/{customerId}/users` | `customerId` | `search, status, memberType, sort, page, pageSize` | `None` | System Administrator |
| **POST** | `/customers/{customerId}/users` | `customerId` | `sendInvitation` | `CreateCustomerUserRequest` | System Administrator |
| **GET** | `/customers/{customerId}/users/{userId}` | `customerId, userId` | `None` | `None` | System Administrator |
| **PUT** | `/customers/{customerId}/users/{userId}` | `customerId, userId` | `None` | `UpdateCustomerUserRequest` | System Administrator |
| **DELETE** | `/customers/{customerId}/users/{userId}` | `customerId, userId` | `None` | `None` | System Administrator |

---

## 7. Marketing Campaigns (Discounts)
Manages discount campaign codes, percentage/fixed pricing deductions, and active timelines.

| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/discounts` | `None` | `search, status, type, applicableTo, startsFrom, startsTo, expiresFrom, expiresTo, sort, page, pageSize` | `None` | System Administrator |

---

## 8. Billing Subscriptions
Controls recurring client payment plan subscriptions, billing loops, and cancellations.

| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/subscriptions` | `None` | `search, status, planId, page, pageSize` | `None` | System Administrator |
| **GET** | `/subscriptions/{subscriptionId}` | `subscriptionId` | `includeHistory` | `None` | System Administrator |
| **POST** | `/subscriptions` | `None` | `None` | `CreateSubscriptionRequest` | System Administrator |
| **PUT** | `/subscriptions/{subscriptionId}` | `subscriptionId` | `None` | `UpdateSubscriptionRequest` | System Administrator |
| **DELETE** | `/subscriptions/{subscriptionId}` | `subscriptionId` | `cancelImmediately` | `None` | System Administrator |

---

## 9. Activation Keys (Licenses)
Generates, validates, and manages licensing API credentials and software access tokens.

| HTTP Method | Route URI | URI parameters | Query Filters & Options | Request DTO | Access Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/licenses` | `None` | `search, status, page, pageSize` | `None` | System Administrator |
| **GET** | `/licenses/{licenseId}` | `licenseId` | `None` | `None` | System Administrator |
| **POST** | `/licenses` | `None` | `None` | `CreateLicenseRequest` | System Administrator |
| **DELETE** | `/licenses/{licenseId}` | `licenseId` | `None` | `None` | System Administrator |
