import tkinter as tk
from tkinter import messagebox
from inventory import inventory, item_Id, low_stock_item, load_inventory, save_inventory, export_to_csv, customError


def show_gui_inventory():
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) >= 6:
            widget.destroy()
    row_num = 6
    for id, item in inventory.items():
        label = tk.Label(root, text=f"ID: {id} | Name: {item['name']} | Price: ₹{item['price']} | Qty: {item['quantity']}")
        label.grid(row=row_num, column=0, columnspan=3, pady=2)
        if item["quantity"] <= 5:
            low_stock_item.add(item["name"])
        row_num += 1
    if low_stock_item:
        tk.Label(root, text=f"Low Stock Items: {', '.join(low_stock_item)}", fg="red").grid(row=row_num, column=0, columnspan=3)

def add_gui_item():
    global item_Id
    try:
        name = name_label.get().strip()
        price = float(price_label.get())
        quantity = int(quantity_label.get())

        if quantity < 0:
            raise customError("Quantity can't be negative")

        inventory[item_Id] = {"name": name, "price": price, "quantity": quantity}
        if quantity <= 5:
            low_stock_item.add(name)

        messagebox.showinfo("Success", f"Item Added!\nID: {item_Id}\nName: {name}")
        item_Id += 1
        save_inventory()
        show_gui_inventory()
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")
    except customError as e:
        messagebox.showerror("Error", str(e))

def remove_gui_item():
    try:
        id = int(id_label.get())
        if id in inventory:
            del inventory[id]
            save_inventory()
            messagebox.showinfo("Success", f"Item {id} removed.")
            show_gui_inventory()
        else:
            messagebox.showwarning("Not Found", f"No item found with ID {id}")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid ID.")

def update_gui_item():
    try:
        id = int(update_label.get())
        if id in inventory:
            def submit_update():
                try:
                    new_price = float(update_price.get()) if update_price.get() else inventory[id]['price']
                    new_qty = int(update_qty.get()) if update_qty.get() else inventory[id]['quantity']
                    inventory[id]['price'] = new_price
                    inventory[id]['quantity'] = new_qty
                    save_inventory()
                    messagebox.showinfo("Updated", f"Item {id} updated.")
                    show_gui_inventory()
                    update_popup.destroy()
                except:
                    messagebox.showerror("Error", "Invalid values.")

            update_popup = tk.Toplevel(root)
            update_popup.title("Update Item")
            tk.Label(update_popup, text="New Price:").grid(row=0, column=0)
            update_price = tk.Entry(update_popup)
            update_price.grid(row=0, column=1)
            tk.Label(update_popup, text="New Quantity:").grid(row=1, column=0)
            update_qty = tk.Entry(update_popup)
            update_qty.grid(row=1, column=1)
            tk.Button(update_popup, text="Submit", command=submit_update).grid(row=2, column=0, columnspan=2, pady=5)
        else:
            messagebox.showwarning("Not Found", f"No item with ID {id}")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid ID.")


def gui_add_form():
    global name_label, price_label, quantity_label
    clear_widgets()
    tk.Label(root, text="Name:").grid(row=6, column=0)
    name_label = tk.Entry(root)
    name_label.grid(row=6, column=1)

    tk.Label(root, text="Price:").grid(row=7, column=0)
    price_label = tk.Entry(root)
    price_label.grid(row=7, column=1)

    tk.Label(root, text="Quantity:").grid(row=8, column=0)
    quantity_label = tk.Entry(root)
    quantity_label.grid(row=8, column=1)

    tk.Button(root, text="Add Item", command=add_gui_item).grid(row=9, column=0, columnspan=2)

def gui_remove_form():
    global id_label
    clear_widgets()
    tk.Label(root, text="Enter ID to remove:").grid(row=6, column=0)
    id_label = tk.Entry(root)
    id_label.grid(row=6, column=1)
    tk.Button(root, text="Remove", command=remove_gui_item).grid(row=7, column=0, columnspan=2)

def gui_update_form():
    global update_label
    clear_widgets()
    tk.Label(root, text="Enter ID to update:").grid(row=6, column=0)
    update_label = tk.Entry(root)
    update_label.grid(row=6, column=1)
    tk.Button(root, text="Update", command=update_gui_item).grid(row=7, column=0, columnspan=2)

def clear_widgets():
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) >= 6:
            widget.destroy()

def start_gui():
    global root
    load_inventory()
    global item_Id
    root = tk.Tk()
    root.title("Inventory Management System")

    tk.Label(root, text="Inventory Management System", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

    tk.Button(root, text="Add Item", width=15, command=gui_add_form).grid(row=1, column=0)
    tk.Button(root, text="Remove Item", width=15, command=gui_remove_form).grid(row=1, column=1)
    tk.Button(root, text="Update Item", width=15, command=gui_update_form).grid(row=1, column=2)
    tk.Button(root, text="Show Inventory", width=15, command=show_gui_inventory).grid(row=2, column=0)
    tk.Button(root, text="Export to CSV", width=15, command=export_to_csv).grid(row=2, column=1)
    tk.Button(root, text="Exit", width=15, command=root.destroy).grid(row=2, column=2)

    root.mainloop()
