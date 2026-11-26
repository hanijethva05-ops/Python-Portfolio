#restaurant bill
menu={
    1:{"name":"Pizza","price":250},
    2:{"name":"Burger","price":120},
    3:{"name":"Pasta","price":180},
    4:{"name":"Sandwich","price":100},
    5:{"name":"French Fries","price":80},
    6:{"name":"Cold Drink","price":50}
    }

order={}

customer=input("Enter Customer Name:")

#display_menu
def display_menu():
    print("-------RESTAURANT MENU---------")
    for key,value in menu.items():
        print(key,value["name"],"Rs.", value["price"])
        
    
#take_order
def take_order():
    while True:
        display_menu()
        item=int(input("Enter Item Number(0 to stop):"))

        if item==0:
            break

        if item not in menu:
            print("Invalid Item Number")
            continue

        qty=int(input("Enter Quantity:"))

        if qty<=0:
            print("Enter Valid Quantity!")
            continue

        if item in order:
            order[item]+=qty
        else:
            order[item]=qty

        print(menu[item]["name"],"added successfully!")

    
#view_order
def view_order():
    if len(order)==0:
        print("No order found!")
        return

    print("\n------YOUR ORDER-------")
    subtotal=0

    for item,qty in order.items():
        name=menu[item]["name"]
        price=menu[item]["price"]
        amount=price*qty
        subtotal+=amount

        print(name,price,qty,amount)

    print("Subtotal:Rs.",subtotal)

#generate_bill
def generate_bill():
    if len(order)==0:
        print("No order found!")
        return

    subtotal=0

    print("\n------RESTAURANT BILL-------")
    print("Customer Name:",customer)

    for item,qty in order.items():
        name=menu[item]["name"]
        price=menu[item]["price"]
        amount=price*qty
        subtotal+=amount

    print(name,"price:",price,"Qty:",qty,"Amount:",amount)

    gst=subtotal*5/100
    final_amount=subtotal+gst

    print("------------------------")
    print("Subtotal: Rs.",subtotal)
    print("GST(5%): Rs.",gst)
    print("Final Amount: Rs.",final_amount)

    print("========================")

#clear_order
def clear_order():
    order.clear()
    print("Order cleared successfully!")


#main program
while True:
    print("\n==============================")
    print(" RESTAURANT BILLING SYSTEM")
    print("==============================")
    print("1.Display Menu")
    print("2.Take Order")
    print("3.View Order")
    print("4.Generate Bill")
    print("5.Clear Order")
    print("6.Exit")

    choice=int(input("Enter Your Choice:"))

    if choice==1:
        display_menu()

    elif choice==2:
        take_order()

    elif choice==3:
        view_order()

    elif choice==4:
        generate_bill()

    elif choice==5:
        clear_order()

    elif choice==6:
        print("Thank you for visiting our restaurant!")
        print("Please visit again.")
        break

    else:
        print("Invalid choice!Please select 1 to 6.")















































































































































