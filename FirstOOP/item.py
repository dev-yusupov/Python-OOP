class Item:
    def __init__(self, name: str, price: float, number: int):

        assert price >= 0, f"Price {price} is not greater than 0"
        assert number >= 0, f"Quantity {number} is not greater than 0"

        self.name = name
        self.price = price
        self.number = number
    
    def __str__(self):
        return f"The price of {self.name} is ${self.price}"
    
    def calculate_price(self):
        self.result = self.price * self.number
        return f"{self.name} is {self.result} in total"

    def remained(self):
        self.total = int(input("Totally: "))

        return f"Remained: {self.total - self.number}"