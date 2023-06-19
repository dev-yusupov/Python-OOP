from product import Product

class Phone(Product):
    payment_rate = 0.6
    def __init__(self, name, price):
        super().__init__(name, price)

    def calculate_price(self, quantity=0):
        return self.price * quantity

phone1 = Phone("iPhone", 300)
phone2 = Phone("Samsung", 200)

print(phone1.payment_rate)
print(phone2.payment_rate)