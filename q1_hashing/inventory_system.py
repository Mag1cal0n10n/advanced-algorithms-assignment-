from hash_table import HashTable
from medicine import Medicine

inv = HashTable(17)

medicines = [
Medicine(1042, "Paracetamol", 5.5, 100),
Medicine(1035, "Ibuprofen", 7.49, 50),
Medicine(2052, "Vitamin C", 12.99, 200),
Medicine(3062, "Cough Syrup", 9.99, 75),
Medicine(4072, "Antibiotic Cream", 15.0, 30),
Medicine(1059, "Antihistamine", 8.5, 60),
Medicine(2053, "Multivitamin", 20.0, 150),
Medicine(3063, "Nasal Spray", 11.0, 40),
Medicine(4073, "Pain Relief Gel", 14.0, 25),
Medicine(1076, "Decongestant", 6.5, 80)
]

for med in medicines:
    result = inv.insert(med.product_id, med)
    print(f"Inserted {med.product_id} ({med.name}) into slot {result}.")

while True:
    print("\n===== HC Pharmacy Inventory System ======")
    print("1. Insert medicine")
    print("2. Search medicine")
    print("3. Display all")
    print("4. Delete medicine")
    print("5. Edit Product Details")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
            # Get medicine details from user
            try:
                product_id = int(input("Enter product ID: "))
                name = input("Enter medicine name: ").strip()
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))
            except ValueError:
                print("Invalid input. Please enter valid data types for product ID, price, and stock.")
                continue
            
            if product_id <= 0 or price <= 0 or stock <= 0:
                print("Product ID, price, and stock must be positive.")
                continue
            
            if name == "":
                print("Medicine name cannot be empty.")
                continue

            if inv.search(product_id) is not None:
                print(f"Medicine with product ID {product_id} already exists.")
                continue

            new_medicine = Medicine(product_id, name, price, stock)
            result = inv.insert(product_id, new_medicine) # Insert the new medicine into the hash table
            if result == -1:
                print("Failed to insert medicine. Table is full.")
            else:
                print(f"Medicine inserted into slot {result}.")

    # Search for a medicine 
    elif choice == '2':
        try:
            product_id = int(input("Enter product ID to search: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for product ID.")
            continue

        medicine = inv.search(product_id)

        if medicine is None:
            print(f"Medicine with product ID {product_id} not found.")
        else:
            print(f"Found: {medicine}")

    elif choice == '3':
        inv.display()

    # Delete a medicine from the inventory
    elif choice == '4':
        try:
            product_id = int(input("Enter product ID to delete: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for product ID.")
            continue

        if inv.delete(product_id):
            print(f"Medicine with product ID {product_id} deleted successfully.")
        else:
            print(f"Medicine with product ID {product_id} not found.")

    elif choice == '5':
        try:
            product_id = int(input("Enter product ID to edit: "))
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
            continue

        medicine = inv.search(product_id)
        if medicine is None:
            print(f"Medicine with product ID {product_id} not found.")
            continue

        print(f"Current details: {medicine}")
        print("\nWhat would you like to modify?")
        print("1. Name\n2. Price\n3. Stock")

        try:
            edit_choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a valid choice (1-3).")
            continue

        # Modify the medicine name   
        if edit_choice == 1:
            new_name = input("Enter new name: ").strip()
            if new_name:
                medicine.name = new_name
                print("Name updated successfully.")
            else:
                print("Name cannot be empty.")

        # Price modification
        elif edit_choice == 2:
            try:
                new_price = float(input("Enter new price: "))
                if new_price > 0:
                    medicine.price = new_price
                    print("Price updated successfully.")
                else:
                    print("Price must be positive.")
            except ValueError:
                print("Invalid input. Please enter a valid price.")

        # Stock modification
        elif edit_choice == 3:
            try:
                new_stock = int(input("Enter new stock quantity: "))
                if new_stock >= 0:
                    medicine.stock = new_stock
                    print("Stock updated successfully.")
                else:
                    print("Stock cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid stock quantity.")

    elif choice == '6':
        print("Have a great day ahead! Goodbye...")
        break
    else:
        print("Invalid choice. Please try again.")
