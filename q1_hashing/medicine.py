class Medicine:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id # int: unique hash table key
        self.name = name # str: name of the medicine
        self.price = price # float: price of the medicine
        self.stock = stock # int: quantity of the medicine in stock

    def __str__(self):
        return f"ID: {self.product_id:<6} | Name: {self.name:<22} | Price: RM{self.price:>7.2f} | Stock: {self.stock:>6}"


if __name__ == "__main__":
    # Example usage
    medicine1 = Medicine(1042, "Paracetamol", 5.5, 100)
    medicine2 = Medicine(1035, "Ibuprofen", 7.49, 50)
    medicine3 = Medicine(2052, "Vitamin C", 12.99, 200)
    medicine4 = Medicine(3062, "Cough Syrup", 9.99, 75)

    print(medicine1)
    print(medicine2)
    print(medicine3)
    print(medicine4)