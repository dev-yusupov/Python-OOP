from item import Item

name = str(input("Name: "))
price = int(input("Price: "))
number = int(input("Number: "))


item = Item(name, price, number)

print(item)