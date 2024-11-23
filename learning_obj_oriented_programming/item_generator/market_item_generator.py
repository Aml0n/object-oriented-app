import csv
import random as r
import time
import os

start_time = time.time()

def name_generator():
    """Generates a random name for the item with silly adjectives and nouns"""
    FirstAdjective = f"{r.choice(['classy', 'colorful', 'trendy', 'fancy', 'spotted', 'wooden', 'interesting', 'soft', 'fuzzy', 'smart'])}"
    SecondAdjective = f"{r.choice(['blue', 'red', 'green', 'yellow', 'purple', 'orange', 'black', 'white', 'grey', 'brown', 'pink', 'beige', 'turquoise'])}"
    ArticleOfClothing = f"{r.choice(['hat', 'shirt', 'pants', 'shoes', 'underwear', 'socks', 'jacket', 'scarf', 'gloves', 'sweater', 'coat', 'dress', 'skirt', 'shorts', 'boots', 'sandals', 'slippers', 'sneakers', 'heels', 'flip-flops'])}"
    return f"{FirstAdjective} {SecondAdjective} {ArticleOfClothing}"

def price_generator():
    """Generates a random price for the item"""
    return round(r.uniform(1, 100), 2)

def quantity_generator():
    """Generates a random quantity for the item"""
    return round(r.uniform(1, 1000), 2)

def id_generator():
    """Creates a 16-digit id for the item, every 4 digits is separated by a '-' 
    Ex. 1004-2454-2454-8748"""
    FirstCount = f"{str(r.randint(0, 9999)).zfill(4)}"
    SecondCount = f"{str(r.randint(0, 9999)).zfill(4)}"
    ThirdCount = f"{str(r.randint(0, 9999)).zfill(4)}"
    FourthCount = f"{str(r.randint(0, 9999)).zfill(4)}"
    return f"{FirstCount}-{SecondCount}-{ThirdCount}-{FourthCount}"

line_counter = 0 # starts counting upward for every new line created
try: # check if the file actually exists
    with open(os.path.join('item_generator', 'output.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Name', 'Price', 'Quantity', 'ID'])  # Add header row before writing data rows
        while True: # keep writing new rows . . .
            writer.writerow([f"{name_generator()}", f"{price_generator()}", f"{quantity_generator()}", f"{id_generator()}"])
            line_counter += 1
            if line_counter == 100: # . . . until there are 100 rows (+ the header row)
                break
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")

end_time = time.time()
elapsed_time = start_time - end_time
print(f"Done. Printed {line_counter} lines in {elapsed_time:.2f}")

