class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")

        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term == contact.phone_number:
                print(contact)
                return

        print("Contact not found.")

    def update_contact(self):
        if not self.contacts:
            print("No contacts found.")
            return

        while True:
            name_to_update = input("Enter the name of the contact to update or 'q' to quit: ")
            if name_to_update.lower() == 'q':
                return
            for i, contact in enumerate(self.contacts):
                if contact.name.lower() == name_to_update.lower():
                    new_name = input("Enter new name: ")
                    new_phone_number = input("Enter new phone number: ")
                    new_email = input("Enter new email: ")
                    new_address = input("Enter new address: ")

                    contact.name = new_name
                    contact.phone_number = new_phone_number
                    contact.email = new_email
                    contact.address = new_address
                    print("Contact updated successfully!")
                    return
            print("Contact not found. Try again!")

    def delete_contact(self):
        if not self.contacts:
            print("No contacts found.")
            return

        while True:
            name_to_delete = input("Enter the name of the contact to delete or 'q' to quit: ")
            if name_to_delete.lower() == 'q':
                return
            for i, contact in enumerate(self.contacts):
                if contact.name.lower() == name_to_delete.lower():
                    del self.contacts[i]
                    print("Contact deleted successfully!")
                    return
            print("Contact not found. Try again!")

 
    
contact_manager = ContactManager()
while True:
        
    print("\nContact Book")
    print("------------------------")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        contact_manager.add_contact()
        
    elif choice == "2":
        contact_manager.view_contacts()
    elif choice == "3":
        contact_manager.search_contact()
    elif choice == "4":
        contact_manager.update_contact()
    elif choice == "5":
        contact_manager.delete_contact()
    elif choice == "6":
        print("Exiting ContactBook...")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")