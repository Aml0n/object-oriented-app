# hello!
# this is my first time working with classes in python
# you'll see lots of "note to self:"s
# because i usually have trouble visualizing code
# especially dictionaries and lists

import csv
import os

class Item:

    def __init__(self, name, price, quantity, id, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = id
        self.category = category

    def __str__(self):
        return f"{self.name}, ${self.price}, {self.quantity}, {self.id}"
    
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}, {self.id})"
    
class Cart:

    def __init__(self):
        self.in_cart = []
        
    def __str__(self):
        return f"{self.in_cart}"

# Dictionary to store items by category
items_by_category = {}
# note to self:
# this will organize the dictionary so it looks more like this
# swimwear :
#   {swimwear_item(. . .)}
#   {swimwear_item(. . .)}
#   {swimwear_item(. . .)}
#   {swimwear_item(. . .)}
# professional
#   {professional_item(. . .)}
#   {professional_item(. . .)}
#   {professional_item(. . .)}
#   {professional_item(. . .)}


# Read items from CSV file
with open(os.path.join('item_generator', '.ignore', 'output.csv'), 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)  # Skip the header row
    for row in reader:
        # print(f"Reading row: {row}")  # Debugging print statement
        item = Item(row[0], float(row[1]), int(row[2]), row[3], row[4])
        if item.category not in items_by_category:
            items_by_category[item.category] = []
        items_by_category[item.category].append(item)
        # print(f"Added {item} to category {item.category}")  # Debugging print statement

# Function to filter items by category
def filter_items_by_category(category):
    return items_by_category.get(category, [])

# # Example usage
# swimwear_items = filter_items_by_category('swimwear')
# print(swimwear_items)
