from hash_table import HashTable
from medicine import Medicine

inv = HashTable(17)

medicines = [
    Medicine(1042, "Paracetamol", 5.5, 100, "Pain Relief"),
    Medicine(1035, "Ibuprofen", 7.49, 50, "Pain Relief"),
    Medicine(2052, "Vitamin C", 12.99, 200, "Supplements"),
    Medicine(3062, "Cough Syrup", 9.99, 75, "Cold & Flu"),
    Medicine(4072, "Antibiotic Cream", 15.0, 30, "Topical Treatments"),
    Medicine(1059, "Antihistamine", 8.5, 60, "Allergy Relief"),
    Medicine(2053, "Multivitamin", 20.0, 150, "Supplements"),
    Medicine(3063, "Nasal Spray", 11.0, 40, "Cold & Flu"),
    Medicine(4073, "Pain Relief Gel", 14.0, 25, "Topical Treatments"),
    Medicine(1076, "Decongestant", 6.5, 80, "Cold & Flu")
]

for med in medicines:
    result = inv.insert(med.product_id, med)
    print(f"Inserted {med.product_id} ({med.name}) into slot {result}.")

inv.display()