import json
import os
class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    def to_dict(self):
        """Converts object to dictionary for JSON storage."""
        return {"name": self.name, "phone": self.phone, "email": self.email}
    def __str__(self):
        return f"{self.name.ljust(15)} | {self.phone.ljust(12)} | {self.email}"
    
class ContactBook:
    def __init__(self,filename = "contacts_data.json"):
        self.filename = filename 
        self.contacts = []
        self.load_from_file()
    def add_contact(self,name,phone,email):
        new_contact = Contact(name,phone,email)
        self.contacts.append(new_contact)
        self.save_to_file()
        print(f"\n Success: {name} added and saved.")
    def remove_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_to_file()
                print(f"\n Removed: {name}")
                return
        print(f"\n Error: '{name}' not found.")
    
    def save_to_file(self):
        """Saves the current list of contacts to a JSON file."""
        with open(self.filename, "w") as f:
            json_data = [c.to_dict() for c in self.contacts]
            json.dump(json_data, f, indent=4)

    def load_from_file(self):
        """Loads contacts from JSON file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.contacts = [Contact(item['name'], item['phone'], item['email']) for item in data]
            except Exception as e:
                print(f"Error loading file: {e}")
        else:
            self.contacts = []
    def show_all(self):
        if not self.contacts:
            print("\n The contact book is empty.")
        else:
            print("\n" + "="*35)
            for contact in self.contacts:
                print(contact)
            print("="*35)

def main():
    book = ContactBook()
    
    while True:
        print("\n--- 📱 PERSISTENT CONTACT BOOK ---")
        print("1. Add  2. Delete  3. Show All  4. Exit")
        choice = input("Select: ")

        if choice == '1':
            book.add_contact(input("Name: "), input("Phone: "), input("Email: "))
        elif choice == '2':
            book.remove_contact(input("Name to delete: "))
        elif choice == '3':
            book.show_all()
        elif choice == '4':
            print("👋 Data saved. Goodbye!")
            break

if __name__ == "__main__":
    main()
