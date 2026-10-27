import time
from linear_search import linear_search
from hash_table import HashTable
from medicine import Medicine

inv = HashTable(41)
med_array = [] # plain one-dimensional array with the same records (comparison)
repeats = 1000


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
    Medicine(1076, "Decongestant", 6.5, 80),
    Medicine(1083, "Loratadine", 9.20, 70),
    Medicine(1124, "Cetirizine", 8.90, 65),
    Medicine(5011, "Omeprazole", 18.50, 40),
    Medicine(5023, "Antacid Tablets", 6.80, 120),
    Medicine(5037, "Oral Rehydration Salts", 4.50, 90),
    Medicine(5049, "Zinc Supplement", 13.40, 55),
    Medicine(6014, "Throat Lozenges", 5.90, 150),
    Medicine(6028, "Antiseptic Liquid", 10.50, 45),
    Medicine(7005, "Hydrocortisone Cream", 16.00, 20),
    Medicine(7019, "Eye Drops", 12.30, 35)

]

for med in medicines:
    result = inv.insert(med.product_id, med)
    med_array.append(med)
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
                med_array.append(new_medicine) 
                print(f"Medicine inserted into slot {result}.")

    # Search for a medicine 
    elif choice == '2':
        try:
            product_id = int(input("Enter product ID to search: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for product ID.")
            continue

        # Time the hash table search
        start = time.perf_counter_ns()
        for _ in range(repeats):
            medicine = inv.search(product_id)
        end = time.perf_counter_ns()
        hash_time = (end - start) / repeats

        # Time the array (linear) search on the same data
        start = time.perf_counter_ns()
        for _ in range(repeats):
            array_result = linear_search(med_array, product_id)
        end = time.perf_counter_ns()
        array_time = (end - start) / repeats

        if medicine is None:
            print(f"Medicine with product ID {product_id} not found.")
        else:
            print(f"Found: {medicine}")

        print(f"Search completed in {hash_time / 1_000_000_000:.9f} seconds (Hash Table)")
        print(f"Search completed in {array_time / 1_000_000_000:.9f} seconds (Array - same record)")

    elif choice == '3':
        inv.display()

    # Delete a medicine from the inventory
    elif choice == '4':
        try:
            product_id = int(input("Enter product ID to delete: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for product ID.")
            continue

        medicine = inv.search(product_id)
        if medicine is None:
            print(f"Medicine with product ID {product_id} not found.")
            continue

        inv.delete(product_id)     # Remove from hash table
        med_array.remove(medicine) # Remove from the array
        print(f"Medicine with product ID {product_id} deleted successfully.")

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
