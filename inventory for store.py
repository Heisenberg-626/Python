'''
Author: Sourav V S
Date: 19-11-2024
This program is to print the item with highest stock value and its value from a list of items in a store.
'''
inventory = [("Laptop",12,45000.0),
             ("Keyboard",17,1200.0),
             ("Mouse",13,655.0),
             ("Headphone",7,1500.0),
             ("Monitor",6,2100.0)]
highest_stock_value = 0
item_with_highest_stock_value = None
for item in inventory:
    item_name, quantity, unit_price = item
    stock_value = quantity * unit_price
    print(f"Item name: {item_name}, Total value: {stock_value}")
    if stock_value > highest_stock_value:
        highest_stock_value = stock_value
        item_with_highest_stock_value = item_name
    print(f"Highest stock value is: {highest_stock_value}")
    print(f"Item with highest stock value is: {item_with_highest_stock_value}")
