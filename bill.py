'''
You are working as a software developer for "CoffeeKutira Restaurant". The restaurant manager has
asked you to create a calculator program to help staff quickly calculate various bill-related operations
for a single item during busy hours. The program should allow staff to choose from 4 operations:
a. Add - Calculate total bill (food cost + tax)
b. Subtract - Calculate discount amount (original bill - discounted bill)
c. Multiply - Calculate total for multiple identical orders
d. Divide - Split bill among customers

'''

print("☕ CoffeeKutira Restaurant Calculator")
print("1. Add (Total Bill)")
print("2. Subtract (Discount Amount)")
print("3. Multiply (Multiple Orders)")
print("4. Divide (Split Bill)")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    food_cost = float(input("Enter food cost: "))
    tax = float(input("Enter tax amount: "))
    total = food_cost + tax
    print("Total Bill Amount = ₹", total)

elif choice == 2:
    original_bill = float(input("Enter original bill amount: "))
    discounted_bill = float(input("Enter discounted bill amount: "))
    discount = original_bill - discounted_bill
    print("Discount Amount = ₹", discount)

elif choice == 3:
    price = float(input("Enter price of one item: "))
    quantity = int(input("Enter quantity: "))
    total = price * quantity
    print("Total Cost = ₹", total)

elif choice == 4:
    total_bill = float(input("Enter total bill amount: "))
    customers = int(input("Enter number of customers: "))
    split = total_bill / customers
    print("Each person pays = ₹", split)

else:
    print("Invalid Choice")



