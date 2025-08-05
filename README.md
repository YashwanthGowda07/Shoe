# Explanation of Shoe.py - Online Shoe Store Program

This program is an online shoe store application that allows customers to browse, select, and purchase shoes. Here's a breakdown of how it works:

## Main Components

### 1. Customer Class
- Handles user accounts and authentication
- Features:
  - `signup()`: Creates new customer accounts
  - `login()`: Authenticates existing users
  - `logout()`: Ends the user session
  - `update_details()`: Lets users modify their personal information

### 2. Shoe Class
- Manages the shoe inventory and shopping process
- Features:
  - `display_shoes()`: Shows available brands and models
  - `order()`: Guides users through selecting shoes
  - `confirm_order()`: Finalizes purchases
  - Payment methods (credit/debit card, UPI, net banking)
  - Order management (view cart, remove items)

## How the Program Works

1. **Starting the Program**:
   - The `main()` function runs first, welcoming users to the store
   - Users can choose to register, login, or exit

2. **User Authentication**:
   - New users can create accounts with personal details
   - Existing users can log in with their credentials

3. **Shopping Process**:
   - Users can browse shoes from 20 brands (Nike, Adidas, etc.)
   - Each brand offers 3 models with different prices
   - Users select:
     - Brand (by number)
     - Model (by name)
     - Size (from available options)
     - Quantity

4. **Cart Management**:
   - Selected items are added to a shopping cart
   - Users can:
     - View cart contents
     - Remove items
     - Change quantities
     - Continue shopping

5. **Checkout Process**:
   - Users confirm their order
   - Enter delivery address
   - Apply discount codes (like "DISCOUNT10" for 10% off)
   - Choose payment method (card, UPI, or net banking)

6. **Payment**:
   - For card payments: Enter card details and verify with OTP
   - For UPI: Enter UPI ID and verify with OTP
   - For net banking: Select bank and verify with OTP
   - After successful payment, an order summary is shown

7. **Order Completion**:
   - Shows final order details
   - Displays total price and delivery address
   - Thanks the customer and ends the session

## Key Features

- **User-Friendly Interface**: Uses emojis and clear prompts
- **Comprehensive Inventory**: 20 brands with 3 models each
- **Secure Payments**: OTP verification for all transactions
- **Cart Management**: Add, remove, or modify items
- **Discount System**: Special codes for savings

## Example Usage

1. User registers or logs in
2. Browses shoes and selects:
   - Brand: Nike (1)
   - Model: Air Jordan
   - Size: 10
   - Quantity: 2
3. Adds to cart and proceeds to checkout
4. Enters address and applies discount code
5. Pays via credit card (enters card details and OTP)
6. Receives order confirmation

This program simulates a complete online shoe shopping experience from account creation to order fulfillment.
