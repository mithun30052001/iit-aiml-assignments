import json

new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# Task 1 — Read the inventory
with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Total number of books:", len(inventory))

# Task 2 — Update inventory
inventory.append(new_book)

# Save updated inventory
with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

# Task 3 — Display the inventory
with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")