import json

FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


def search_contact(contacts):
    name = input("Enter name to search: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact Found")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")

            save_contacts(contacts)

            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            contacts.remove(contact)
            save_contacts(contacts)

            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n===== CONTACTS =====")

    for contact in contacts:
        print("\nName :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


contacts = load_contacts()

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        search_contact(contacts)

    elif choice == "3":
        update_contact(contacts)

    elif choice == "4":
        delete_contact(contacts)

    elif choice == "5":
        display_contacts(contacts)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")