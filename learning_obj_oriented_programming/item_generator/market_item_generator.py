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
    return r.randint(1, 20)

def id_generator():
    """Creates a 16-digit id for the item, every 4 digits is separated by a '-' 
    Ex. 1004-2454-2454-8748"""
    FirstCount = f"{str(r.randint(0, 9999)).zfill(4)}"
    SecondCount = f"{str(r.randint(0, 9999)).zfill(4)}"
    ThirdCount = f"{str(r.randint(0, 9999)).zfill(4)}"
    FourthCount = f"{str(r.randint(0, 9999)).zfill(4)}"
    return f"{FirstCount}-{SecondCount}-{ThirdCount}-{FourthCount}"

def category_generator():
    """Chooses a random category from sports, professional, casual, sleepwear, and exclusive"""
    return f"{r.choice(['sports', 'professional', 'casual', 'sleepwear', 'exclusive', 'swimwear', 'party'])}"

new_lines = 0 # starts counting upward for every new line created
try: # check if the file actually exists
    with open(os.path.join('item_generator', '.ignore', 'output.csv'), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if csvfile.tell() == 0:
            writer.writerow(['name', 'price', 'quantity', 'id', 'category'])  # Add header row before writing data rows
        while new_lines < 300: # keep writing new rows until x new lines have been written
            writer.writerow([f"{name_generator()}", f"{price_generator()}", quantity_generator(), new_lines, f"{category_generator()}"])
            new_lines += 1
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")

end_time = time.time()
elapsed_time = start_time - end_time
print(f"Done. Printed {new_lines} lines in {elapsed_time:.2f}")