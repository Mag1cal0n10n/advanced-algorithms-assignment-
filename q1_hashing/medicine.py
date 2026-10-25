class Medicine:
    def __init__(self, product_id, name, price, stock, category):
        self.product_id = product_id # int: unique hash table key
        self.name = name # str: name of the medicine
        self.price = price # float: price of the medicine
        self.stock = stock # int: quantity of the medicine in stock
        self.category = category # str: category of the medicine (e.g., "Pain Relief", "Supplements", etc.)

    def __str__(self):
        return f"Medicine(ID: {self.product_id}, Name: {self.name}, Price: {self.price:.2f}, Stock: {self.stock}, Category: {self.category})"


if __name__ == "__main__":
    # Example usage
    medicine1 = Medicine(1042, "Paracetamol", 5.5, 100, "Pain Relief")
    medicine2 = Medicine(1035, "Ibuprofen", 7.49, 50, "Pain Relief")
    medicine3 = Medicine(2052, "Vitamin C", 12.99, 200, "Supplements")
    medicine4 = Medicine(3062, "Cough Syrup", 9.99, 75, "Cold & Flu")

    print(medicine1)
    print(medicine2)
    print(medicine3)
    print(medicine4)