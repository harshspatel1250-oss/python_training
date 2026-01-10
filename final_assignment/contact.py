'''Develop a Python program to manage a contact book.
Allow users to add new contacts, search for contacts by name, and delete contacts.
Use a dictionary to store contacts where the keys are contact names and the values are dictionaries containing contact information like phone number, email, etc.
Implement error handling for cases where a contact is not found during search or deletion.
'''

contact_book = {}

def get_valid_phone():
    while True:
        phone = input("Enter 10-digit phone number: ").strip()
        if phone.isdigit() and len(phone) == 10:
            return phone
        else:
            print("Invalid phone number! Please enter exactly 10 digits.")

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = get_valid_phone()
    email = input("Enter email address: ").strip()

    contact_book[name] = {
        "phone": phone,
        "email": email
    }
    print("Contact added successfully.")

def search_contact():
    name = input("Enter contact name to search: ").strip()
    try:
        contact = contact_book[name]
        print("\nContact Details:")
        print("Name:", name)
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
    except KeyError:
        print("Error: Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    try:
        del contact_book[name]
        print("Contact deleted successfully.")
    except KeyError:
        print("Error: Contact not found.")

def view_all_contacts():
    if not contact_book:
        print("No contacts available.")
        return
    print("\n--- CONTACT LIST ---")
    for name, details in contact_book.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        view_all_contacts()
    elif choice == "5":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")

