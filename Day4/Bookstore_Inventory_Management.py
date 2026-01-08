'''Description: 
Program should contain add_book function which ask user name of book and in second line quantity of book. Add it in inventory dictionary
display_inventory: Print all books currently in dict
update_book_quantity: input book_name and updated quantity and update in dictionary.
Application should keep running until user wants to exit
Main Options:
1. Add a book to inventory
2. Display current inventory
3. Update book quantity
4. Exit'''


# dictionary
inventory = {}

# add
def add_book():
    book_name = input("Enter book name: ")
    quantity = int(input("Enter quantity: "))
    inventory[book_name] = quantity
    print("Book added successfully!\n")

#display
def display_inventory():
    if not inventory:
        print("Inventory is empty.\n")
    else:
        print("Current Inventory:")
        for book, qty in inventory.items():
            print(book, ":", qty)
        print()
#update
def update_book_quantity():
    book_name = input("Enter book name to update: ")
    if book_name in inventory:
        quantity = int(input("Enter updated quantity: "))
        inventory[book_name] = quantity
        print("Quantity updated successfully!\n")
    else:
        print("Book not found in inventory.\n")

while True:
    print("===== Bookstore Inventory Management =====")
    print("1. Add a book to inventory")
    print("2. Display current inventory")
    print("3. Update book quantity")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_inventory()
    elif choice == "3":
        update_book_quantity()
    elif choice == "4":
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.\n")
