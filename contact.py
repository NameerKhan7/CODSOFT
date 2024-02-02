class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
            return

        print("Contact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}\tPhone: {contact.phone}")

    def search_contact(self, search_term):
        for contact in self.contacts:
            if contact.name == search_term or contact.phone == search_term:
                print("Contact found:")
                print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}")
                return
        print("Contact not found.")

    def update_contact(self, name, new_contact):
        for contact in self.contacts:
            if contact.name == name:
                contact.__dict__.update(new_contact.__dict__)
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        if len(self.contacts) < len(self.contacts):
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_contact = Contact(
                input("Enter Name: "),
                input("Enter Phone: "),
                input("Enter Email: "),
                input("Enter Address: "),
            )
            contact_manager.add_contact(new_contact)
        elif choice == 2:
            contact_manager.view_contact_list()
        elif choice == 3:
            search_term = input("Enter name or phone to search: ")
            contact_manager.search_contact(search_term)
        elif choice == 4:
            name = input("Enter the name of the contact to update: ")
            new_contact = Contact(
                input("Enter new Name: "),
                input("Enter new Phone: "),
                input("Enter new Email: "),
                input("Enter new Address: "),
            )
            contact_manager.update_contact(name, new_contact)
        elif choice == 5:
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
