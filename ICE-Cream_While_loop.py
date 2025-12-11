print("Welcome To the Ice-Cream Parlour!")
print("----------- MENU-----------")
print("1. Vanilla Scoop - 40")
print("2. Chocolate Scoop - 55")
print("3. Strawberry Scoop - 60")
print("4. Butterscotch Scoop - 55")
print("---------------------------")

totalBill = 0
orderMode = "yes"

while orderMode.lower() == "yes":
    choice = int(input("Enter Your Choice (1-4): "))
    quantity = int(input("Enter the Quantity: "))

    if choice == 1:
        totalBill += 40 * quantity
        print("You ordered Vanilla Scoop x", quantity)

    elif choice == 2:
        totalBill += 55 * quantity
        print("You ordered Chocolate Scoop x", quantity)
    
    elif choice == 3:
        totalBill += 60 * quantity
        print("You ordered Strawberry Scoop x", quantity)

    elif choice == 4:
        totalBill += 55 * quantity
        print("You ordered Butterscotch Scoop x", quantity)

    else: 
        print("Invalid choice! Please select between 1 and 4.")

    # <-- Moved inside the loop
    orderMode = input("Do you want to order more? (Yes/No): ")

# After loop ends
tax = totalBill * 0.08
finalBill = totalBill + tax

print("\n----------- BILL -----------")
print("Total before tax: ", totalBill)
print("8% tax: ", round(tax, 2))
print("Final Bill Amount: ", round(finalBill, 2))
print("----------------------------")
print("Thank You for visiting our Ice-Cream Parlour!")