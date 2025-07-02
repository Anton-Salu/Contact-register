import sqlite3

# Connect to SQLite (or create the database file)
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT
    )
""")
conn.commit()

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    print("Contact added successfully!")

def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    print("\n📋 Contact List:")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")
    print()

def update_contact():
    view_contacts()
    contact_id = input("Enter the ID of the contact to update: ")
    new_name = input("Enter new name: ")
    new_phone = input("Enter new phone: ")
    new_email = input("Enter new email: ")
    cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?",
                   (new_name, new_phone, new_email, contact_id))
    conn.commit()
    print("Contact updated successfully!")

def delete_contact():
    view_contacts()
    contact_id = input("Enter the ID of the contact to delete: ")
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    print("Contact deleted successfully!")

def menu():
    while True:
        print("""
📱 Personal Contact Book
-------------------------
1. Add New Contact
2. View All Contacts
3. Update Contact
4. Delete Contact
5. Exit
""")
        choice = input("Choose an option (1–5): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    menu()
    conn.close()