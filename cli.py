from inventory import inventory, item_Id, low_stock_item, load_inventory, save_inventory, export_to_csv, customError


def low_stock():
    if len(low_stock_item) != 0 :
        print("\nTHis Items are running low on stock : ")
        for item  in low_stock_item :
            print(item , "\n")
        

def add_item():
        global item_Id 
        try:

            name = input('Enter the name of the item. ')
            price = float(input("Enter the price of the "+ name + " : "))
            quantity = int(input("Enter the quantity of the "+  name +" : "))
            inventory[item_Id] = {
                "name": name, 
                "price": price,
                "quantity": quantity
            }
            if(quantity <  0):
                raise customError("")
            
            print("\n\nItem name : ",name,"\nItem Id : " , item_Id, "\nItem price : ", price , "\nItem quantity : " , quantity)
            item_Id += 1

            if(quantity <= 5):
                low_stock_item.add(name)
            low_stock()
            save_inventory()
        except customError as e:
            print("Cought an Error : Negative Quantity not allowed. -_-  ")

    
def remove_itme():
    id = int(input('Enter the Id of the item you want to remove : '))
        
    if id in inventory:
        del inventory[id]
        print('Item deleated')
    else:
        print('Item not found')
    save_inventory()


def Show_itme():
    for id in inventory:
        item = inventory[id]
        print("\nID : " , id)
        print("Name : ",item["name"])
        print("Price : ",item["price"])
        print("Quantity : ",item["quantity"])
        print("\n")
        
        if(item["quantity"] <= 5):
            low_stock_item.add(item["name"])
    low_stock()
        
    


def Search_item():
    key = int(input('Enter the Id of the item you want to search. \n'))
    if key not in inventory : 
        print("\nNo item present at this Id.\n")
    else:
        print("\nItem found!\n")
        print("Name : " , inventory[key]["name"])
        print("Price : " , inventory[key]["price"])
        print("Quantity : " , inventory[key]["quantity"])
        print("\n")


def Update_item():
    id = int(input("Enter the Id of the element you want to update. "))
    if id in inventory:
        try:
            print("\nFound It ! ")
            print("To update price press 1. ")
            print("To update the quantity of your item press 2.")
            print("To update both press 3. ")
            choice = int(input())
            if(choice > 3):
                raise customError("")
            elif(choice == 1):
                new_price = input("Enter the new Price. ")
                if new_price != "":
                    new_price = float(new_price)
                else:
                    new_price = inventory[id]['price']
                inventory[id]['price'] = new_price
            elif(choice == 2):
                new_quantity = input("Enter the new Quantity. ")
                if new_quantity != "":
                    new_quantity = int(new_quantity)
                else:
                    new_quantity = inventory[id]['quantity']
                inventory[id]['quantity'] = new_quantity
            elif(choice == 3):
                new_price = input("Enter the new Price. ")
                if new_price != "":
                    new_price = float(new_price)
                else:
                    new_price = inventory[id]['price']

                new_quantity = input("Enter the new Quantity. ")
                if new_quantity != "":
                    new_quantity = int(new_quantity)
                else:
                    new_quantity = inventory[id]['quantity']

                inventory[id]['price'] = new_price
                inventory[id]['quantity'] = new_quantity
            print("\nVAlues Updated . ")
            save_inventory()
        except ValueError as e:
            print("Please Enter a integer as a choice. -_- ")
        except customError as e:
            print("Error Cought ! Please Enter a valid choice. -_- ")
    else:
        print("Id not found!")


def cli_main():
    load_inventory()
    while True:
        try:
            print('\nWelcome to the Inverntry Management System. :) ')
            print("Please Select your option :- ")
            print('1. Add itme to inventry.')
            print('2. Remove itme to inventry.')
            print('3. Show itmes present in the inventry.')
            print('4. Search a perticular Itmen.')
            print('5. Update an Existing Item.')
            print('6. Export to csv.')
            print('7. Exit.')

            choice = int(input())
            if(choice == 1 ):
                add_item()
            elif(choice == 2):
                remove_itme()
            elif(choice == 3):
                Show_itme()
            elif(choice == 4):
                Search_item()
            elif(choice == 5):
                Update_item()
            elif(choice == 6):
                export_to_csv()
            elif(choice == 7):
                print("\n Exiting ... \n")
                break
            else:
                print('Please enter a valid choice -_-\n')
        except ValueError:
            print("Enter a valid Input")  