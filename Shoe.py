import random
import time

class Customer:
    cus_details = {}
    
    def __init__(self,username,password,name,phone,address,email):
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
    
    def signup(self):
        if self.username in Customer.cus_details:
            print('User already exists')
            print('Please login')
            self.login()
        else:
            print('User entering first time')
            print('Create a account')
            print('Enter your details')
            username = input('👤 Enter your username: ')
            password = input('🔑 Enter your password: ')
            name = input('🧑 Enter your name: ')
            phone = input('📱 Enter your phone number: ')
            address = input('📍 Enter your address: ')
            email = input('📧 Enter your email: ')
            Customer.cus_details[username] = {
                'password': password,
                'name': name,
                'phone': phone,
                'address': address,
                'email': email
            }
            print('✅ Account created successfully')
            print('Please login to continue')
            self.login()
        
    def login(self):
        print('Login to yur account')
        username = input('👤 Enter your username: ')
        if username in self.cus_details:
            if username == self.username:
                password = input('🔑 Enter your password: ')
                if password == self.password:
                    print('✅ Login successful')
                    print(f'Welcome {self.name}')
                else:
                    print('Incorrect password')
                    print('Please try again')
                    self.login()
            else:
                print('Username not found')
                print('Please try again')
                self.login()
        else:
            print('Username not found')
            print('Please register first')
            self.signup()
            
    def logout(self):
        print('You have been logged out')
        print('Thank you for visiting')
        print('Have a great day!')
    
    def update_details(self):
        print('Update your details')
        print('Which detail do you want to update?')
        print('1. Name')
        print('2. Phone')
        print('3. Address')
        print('4. Email')
        choice = int(input('Enter your choice (1-4): '))
        if choice == 1:
            new_name = input('Enter your new name: ')
            self.name = new_name
            Shoe.cus_details[self.username]['name'] = new_name
            print('✅ Name updated successfully')
        elif choice == 2:
            new_phone = input('Enter your new phone number: ')
            self.phone = new_phone
            Shoe.cus_details[self.username]['phone'] = new_phone
            print('✅ Phone number updated successfully')
        elif choice == 3:
            new_address = input('Enter your new address: ')
            self.address = new_address
            Shoe.cus_details[self.username]['address'] = new_address
            print('✅ Address updated successfully')
        elif choice == 4:
            new_email = input('Enter your new email: ')
            self.email = new_email
            Shoe.cus_details[self.username]['email'] = new_email
            print('✅ Email updated successfully')
        else:
            print('Invalid choice')
            print('Please try again')
            self.update_details()

class Shoe:
    
    company = {1: 'Nike', 2: 'Adidas', 3: 'Puma', 4: 'Reebok', 5: 'Under Armour',6:'Campus',7:'Bata',8:'Woodland',9:'Sparx',10:'Red Tape',11:'Fila',12:'ASICS',13:'New Balance',14:'Skechers',15:'Converse',16:'Vans',17:'Hush Puppies',18:'Clarks',19:'Timberland',20:'Dr. Martens'}
    models = {1: {'Air Max': 10000, 'Air Force 1': 9000, 'Air Jordan': 12000},
              2: {'Ultraboost': 11000, 'NMD': 9500, 'Superstar': 8000},
              3: {'RS-X': 8500, 'Future Rider': 8000, 'Clyde': 7500},
              4: {'Classic Leather': 7000, 'Club C': 6500, 'Zig Kinetica': 9000},
              5: {'HOVR Phantom': 12000, 'Charged Impulse': 10000, 'Micro G Pursuit': 8000},
              6: {'Campus': 6000, 'Superstar': 7000, 'Gazelle': 6500},
              7: {'Bata Casual': 5000, 'Bata Formal': 6000, 'Bata Sports': 5500},
              8: {'Woodland Hiking': 8000, 'Woodland Casual': 7000, 'Woodland Formal': 7500},
              9: {'Sparx Sports': 4000, 'Sparx Casual': 3500, 'Sparx Formal': 3000},
              10: {'Red Tape Casual': 6000, 'Red Tape Formal': 7000, 'Red Tape Sports': 6500},
              11: {'Fila Disruptor': 8000, 'Fila Ray': 7500, 'Fila Original': 7000},
              12: {'ASICS Gel-Kayano': 12000, 'ASICS Gel-Nimbus': 11000, 'ASICS Gel-Quantum': 10000},
              13: {'New Balance 990': 13000, 'New Balance 574': 12000, 'New Balance Fresh Foam': 11000},
              14: {'Skechers Go Walk': 8000, "Skechers D'Lites": 7500, 'Skechers Flex Appeal': 7000},
              15: {'Converse Chuck Taylor': 5000, 'Converse One Star': 5500, 'Converse All Star': 6000},
              16: {'Vans Old Skool': 6000, 'Vans Authentic': 5500, 'Vans Slip-On': 5000},
              17: {'Hush Puppies Formal': 7000, 'Hush Puppies Casual': 6500, 'Hush Puppies Sports': 6000},
              18: {'Clarks Desert Boot': 8000, 'Clarks Wallabee': 7500, 'Clarks Trigenic': 7000},
              19: {'Timberland Classic 6-Inch': 12000, 'Timberland Euro Hiker': 11000, 'Timberland Chukka': 10000},
              20: {'Dr. Martens 1460': 13000, 'Dr. Martens 1461': 12000, 'Dr. Martens Pascal': 11000}}
    
    @staticmethod
    def size():
        size = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        return size
    
    @staticmethod
    def display_shoes():
        print("Available Shoe Brands and Models:")
        for brand_id, brand in Shoe.company.items():
            print(f"{brand_id}. {brand}")
            for model, price in Shoe.models[brand_id].items():
                print(f"   - {model}: ₹{price}")
    
    def __init__(self):
        self.price = 0
        self.cart = {}
        
    def welcome(self):
        print("-*4 👟 Welcome to the Shoe Store! 👟 -*4")

    def order(self):
        self.welcome()
        Shoe.display_shoes()
        print("Please select a brand by entering the corresponding number:")
        brand_id = int(input())
        if brand_id not in Shoe.company:
            print("Invalid brand selection. Please try again.")
            return self.order()
        else:
            print(f"You have selected {Shoe.company[brand_id]}")
            print("Please select a model:")
            models = Shoe.models[brand_id]
            for model, price in models.items():
                print(f"{model}: ₹{price}")
            model_name = input("Enter the model name: ")
            if model_name not in models:
                print("Invalid model selection. Please try again.")
                return self.order()
            else:
                print(f"You have selected {model_name} priced at ₹{models[model_name]}")
                print("Please select a size from the following options:")
                size = int(input("Available sizes: " + ", ".join(map(str, Shoe.size())) + "\nEnter size: "))
                quantity = int(input("Enter quantity: "))
                if size not in Shoe.size():
                    print('Invalid size selection. Please try again.')
                    return self.order()
                else:
                    print(f"You have selected size {size} and quantity {quantity}")
                    time.sleep(1)
                    print("Adding to cart...")
                    time.sleep(1)
                    self.cart[self.company[brand_id]] = {
                        'model': model_name,
                        'size': size,
                        'quantity': quantity,
                        'price': models[model_name]
                    }
                    self.price = models[model_name] * quantity
                    print(f"Added to cart: {self.cart}")
                    print(f"Total price: ₹{self.price}")
                    self.confirm_order()
    
    def confirm_order(self):
        print('Do you want to confirm your order? (yes/no)')
        confirm = input().strip().lower()
        if confirm == 'yes':
            print(f"Order confirmed. Total price: ₹{self.price}")
            print('Moving to selecting address...')
            time.sleep(1)
            self.address()
        elif confirm == 'no':
            print('Do you want to continue shopping? (yes/no)')
            cont = input().strip().lower()
            if cont == 'yes':
                print('Continuing shopping...')
                print('Do you want to add more items to your cart? (yes/no)')
                add_more = input().strip().lower()
                if add_more == 'yes':
                    self.order()
                elif add_more == 'no':
                    print('Do you want to clear your cart? (yes/no)')
                    clear_cart = input().strip().lower()
                    if clear_cart == 'yes':
                        self.cart.clear()
                        print('Cart cleared.')
                        print('Do you want to order again? (yes/no)')
                        order_again = input().strip().lower()
                        if order_again == 'yes':
                            self.order()
                        else:
                            print('Thank you for visiting the Shoe Store!')
                    else:
                        print('Do you want to remove an item from your cart? (yes/no)')
                        remove_item = input().strip().lower()
                        if remove_item == 'yes':
                            self.remove_item()
                        else:
                            self.confirm_order()
            else:
                print('Thank you for visiting the Shoe Store!')
        else:
            print('Invalid input. Please try again.')
            self.confirm_order()
            
    def remove_item(self):
        print('You want to remove an item from your cart? (yes/no)')
        remove = input().strip().lower()
        if remove == 'yes':
            print('Which item do you want to remove? (enter the item brand and model)')
            item_brand = input('Brand: ')
            if item_brand in self.cart:
                item_model = input('Enter the model you want to modify:')
                if item_model in self.cart[item_brand][item_model]:
                    print('Do you want to change the quantity or remove the item? (change/remove)')
                    action = input().strip().lower()
                    if action == 'change':
                        new_quantity = int(input('Enter the new quantity: '))
                        self.cart[item_brand][item_model]['quantity'] = new_quantity
                        print(f'Updated quantity for {item_brand} {item_model} to {new_quantity}')
                        self.price = self.cart[item_brand][item_model]['price'] * new_quantity
                        print(f'Total price updated to ₹{self.price}')
                    elif action == 'remove':
                        del self.cart[item_brand][item_model]
                        print(f'Removed {item_brand} {item_model} from cart')
                        if not self.cart[item_brand]:
                            del self.cart[item_brand]
                        print('Cart after removal:', self.cart)
                else:
                    print('Model not found in cart. Please try again.')
                    self.remove_item()
            else:
                print('Brand not found in cart. Please try again.')
                self.remove_item()
        else:
            print('No items removed from cart.')
            self.confirm_order()
    
    def address(self):
        print('Please enter your address details:') 
        address = input('🏠 Address: ')
        print('You have entered the address:', address)
        print('Do you have a discount code? (yes/no)')
        discount_code = input().strip().lower()
        if discount_code == 'yes':
            print('You have a discount code.')
            self.discount()
        else:
            print('No discount code applied.')
            self.payment()
    
    def discount(self):
        print('Please enter your discount code:')
        code = input('🔖 Discount Code: ')
        if code == 'DISCOUNT10':
            discount_amount = self.price * 0.10
            self.price -= discount_amount
            print(f'✅ Discount applied! You saved ₹{discount_amount}. New total price: ₹{self.price}')
        else:
            print('Invalid discount code. No discount applied.')
        self.payment()
    
    def payment(self):
        print('You have entered for payment')
        print(f'Total amount to be paid: ₹{self.price}')
        print('Do you want to view your cart? (yes/no)')
        view_cart = input().strip().lower()
        if view_cart == 'yes':
            self.view_cart()
        else:
            print('Please select a payment method:')
            print('1. Credit/Debit Card')
            print('2. UPI')
            print('3. Net Banking')
            payment_method = input('Enter the number of your choice: ')
            if payment_method == '1':
                print('You have selected Credit/Debit Card')
                self.card_payment()
            elif payment_method == '2':
                print('You have selected UPI')
                self.upi_payment()
            elif payment_method == '3':
                print('You have selected Net Banking')
                self.net_banking_payment()
            else:
                print('Invalid payment method. Please try again.')
                self.payment()
            
    def card_payment(self):
        print('Do you want to pay with Credit cards or Debit cards? (credit/debit)')
        card_type = input().strip().lower()
        if card_type == 'credit':
            self.credit_card_payment()
        elif card_type == 'debit':
            self.debit_card_payment()
        else:
            print('Invalid card type. Please try again.')
            self.card_payment()
    
    def credit_card_payment(self):
        print('💳 You have selected Credit Card payment')
        card_number = input('Enter your last 6 digits credit card number: ')
        expiry_date = input('Enter your credit card expiry date (MM/YY): ')
        cvv = input('Enter your credit card CVV: ')
        if len(card_number) == 6 and len(cvv)==3:
            print('OTP sent to your registered mobile number.')
            time.sleep(10)
            otp = random.randint(100000, 999999)
            print(f'Your OTP is: {otp}')
            entered_otp = int(input('Enter the received OTP: '))
            if entered_otp == otp:
                print('Payment Processing....')
                time.sleep(30)
                print('✅ Payment Successful!')
                print(f'Thank you for your purchase! Total amount paid: ₹{self.price}')
                self.order_summary()
            else:
                print('❌ Invalid OTP. Payment failed.')
                self.credit_card_payment()
        else:
            print('❌ Invalid card details. Please try again.')
            self.credit_card_payment()
    
    def debit_card_payment(self):
        print('💳 You have selected Debit Card payment')
        card_number = input('Enter your last 6 digits debit card number: ')
        expiry_date = input('Enter your debit card expiry date (MM/YY): ')
        cvv = input('Enter your debit card CVV: ')
        if len(card_number) == 6 and len(cvv)==3:
            print('OTP sent to your registered mobile number.')
            time.sleep(10)
            otp = random.randint(100000, 999999)
            print(f'Your OTP is: {otp}')
            entered_otp = int(input('Enter the received OTP: '))
            if entered_otp == otp:
                print('Payment Processing....')
                time.sleep(30)
                print('✅ Payment Successful!')
                print(f'Thank you for your purchase! Total amount paid: ₹{self.price}')
                self.order_summary()
            else:
                print('❌ Invalid OTP. Payment failed.')
                self.debit_card_payment()
        else:
            print('❌ Invalid card details. Please try again.')
            self.debit_card_payment()
    
    def upi_payment(self):
        print('You have selected UPI payment')
        upi_id = input('Enter your UPI ID: ')
        if '@' in upi_id:
            print('UPI ID is valid.')
            print('OTP sent to your registered mobile number.')
            time.sleep(10)
            otp = random.randint(100000, 999999)
            print(f'Your OTP is: {otp}')
            entered_otp = int(input('Enter the received OTP: '))
            if entered_otp == otp:
                print('Payment Processing....')
                time.sleep(30)
                print('✅ Payment Successful!')
                print(f'Thank you for your purchase! Total amount paid: ₹{self.price}')
                self.order_summary()
            else:
                print('❌ Invalid OTP. Payment failed.')
                self.upi_payment()
        else:
            print('❌ Invalid UPI ID. Please try again.')
            self.upi_payment()
    
    def net_banking_payment(self):
        print('You have selected Net Banking payment')
        bank_name = input('Enter your bank name: ')
        if bank_name:
            print(f'You have selected {bank_name} for Net Banking.')
            print('OTP sent to your registered mobile number.')
            time.sleep(10)
            otp = random.randint(100000, 999999)
            print(f'Your OTP is: {otp}')
            entered_otp = int(input('Enter the received OTP: '))
            if entered_otp == otp:
                print('Payment Processing....')
                time.sleep(30)
                print('✅ Payment Successful!')
                print(f'Thank you for your purchase! Total amount paid: ₹{self.price}')
                self.order_summary()
            else:
                print('❌ Invalid OTP. Payment failed.')
                self.net_banking_payment()
        else:
            print('❌ Invalid bank name. Please try again.')
            self.net_banking_payment()
    
    def view_cart(self):
        if self.cart:
            print("Your Cart:")
            for brand, details in self.cart.items():
                print(f"Brand: {brand}, Model: {details['model']}, Size: {details['size']}, Quantity: {details['quantity']}, Price per item: ₹{details['price']}")
            print(f"Total Price: ₹{self.price}")
            self.payment()
        else:
            print("Your cart is empty.")
            print("Please add items to your cart before viewing.")
            self.order()
            
    def order_summary(self):
        print("Order Summary:")
        for brand, details in self.cart.items():
            print(f"Brand: {brand}, Model: {details['model']}, Size: {details['size']}, Quantity: {details['quantity']}, Price per item: ₹{details['price']}")
        print(f"💸 Total Price: ₹{self.price}")
        print('Your address details are:')
        print(f"📍 Address: {self.address}")
        print("Thank you for shopping with us!")
        print('You will receive an email confirmation shortly.')
        print("We hope to see you again soon!")
        print("Have a great day!")
    
def main():
    print("-*4 🛒 Welcome to our online store! 🛒 -*4")
    username = input("👤 Enter your username: ")
    password = input("🔑 Enter your password: ")
    name = input("🧑 Enter your name: ")
    address = input("📍  Enter your address: ")
    phone = input("📱 Enter your phone number: ")
    email = input("📧 Enter your email: ")
    customer = Customer(username, password, name, phone, address, email)
    shoe = Shoe()
    print('-*4 You can choose -*4')
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        customer.signup()
        print('Welcome to the Shoe Store!')
        print('You can choose to order shoes now.')
        print('1. Order Shoes')
        print('2. View Cart')
        print('3. Update Details')
        print('4. Logout')
        action = input('Enter your choice: ')
        if action == '1':
            shoe.display_shoes()
            shoe.order()
        elif action == '2':
            shoe.view_cart()
        elif action == '3':
            customer.update_details()
        elif action == '4':
            customer.logout()
        else:
            print('Invalid choice. Please try again.')
            main()
    elif choice == '2':
        customer.login()
        print('Welcome to the Shoe Store!')
        print('You can choose to order shoes now.')
        print('1. Order Shoes')
        print('2. View Cart')
        print('3. Update Details')
        print('4. Logout')
        action = input('Enter your choice: ')
        if action == '1':
            shoe.display_shoes()
            shoe.order()
        elif action == '2':
            shoe.view_cart()
        elif action == '3':
            customer.update_details()
        elif action == '4':
            customer.logout()
        else:
            print('Invalid choice. Please try again.')
            main()
    elif choice == '3':
        customer.logout()
    else:
        print('Invalid choice. Please try again.')
        main()

main()