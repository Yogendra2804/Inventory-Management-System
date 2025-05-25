import json
import csv

inventory = {}
item_Id = 1
low_stock_item = set()

class customError(Exception):
    def __init__(self, message="Invalid Input"):
        super().__init__(message)

def load_inventory():
    global inventory, item_Id
    try:
        with open("inventory.json", "r") as f:
            loaded = json.load(f)
            inventory = {int(k): v for k, v in loaded.items()}
        item_Id = max(inventory.keys()) + 1 if inventory else 1
    except FileNotFoundError:
        inventory = {}

def save_inventory():
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

def export_to_csv():
    with open("inventory_export.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Price", "Quantity"])
        for id, item in inventory.items():
            writer.writerow([id, item["name"], item["price"], item["quantity"]])
