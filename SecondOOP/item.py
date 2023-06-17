from product import Product

product_name = str(input("Product Name: "))
product_price = int(input("Price: "))
quantity = int(input("Quantity: "))

class Phone(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def calculate_price(self, quantity=0):
        return self.price * quantity

phone = Phone(product_name, product_price)

print(phone)
print(phone.calculate_price(quantity))