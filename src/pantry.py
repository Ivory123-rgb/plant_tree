def get_storage_method():
    while True:
        print("---------- Storage Method  --------------------")

        print("1.) Pantry/Room Temp")
        print("2.) Freezer")
        print("3.) Refrigerator")
        print("4.) cool dark pantry")
        print("5.) Dehydration")
        print("6.) Canning")
        print("7.) Pickling")
        print("8.) Herb Vase Method")
        print("9.) Fermenting")
        print("10.) Vacuum Sealed")


        choice = input("Select option: ")
        if choice == "1":
            return "Pantry/Room Temp"

        elif choice == "2":
            return "Freezer"

        elif choice == "3":
            return "Refrigerator"
            
        elif choice == "4":
            return "Cool Dark Pantry"


        elif choice == "5":
            return "Dehydration"

            
        elif choice == "6":
            return "Canning"


        elif choice == "7":
            return "Pickling"

            
        elif choice == "8":
            return "Herb Vase Method"


        elif choice == "9":
            return "Fermenting"

            
        elif choice == "10":
            return "Vaccuum Sealed"


        elif choice == "11":
            return home

            

        else:
            print("Invalid selection")





def get_storage_date():
    while True:
        storage_date = input("Enter Storage Date (yyyy-MM-DD):")

        section_date = storage_date.split("-")

        if len(storage_date) == 3 and all(storage_date.isdigit() for section in section_date):
            return storage_date

        print("Invalid. Use YYYY-MM-DD format.")








def add_to_pantry(username):
    auth.load_users()

    print("------------------Pantry Items Added ------------------------")

    produce = input("Produce Type: ")
    storage_method = get_storage_method()
    storage_date = get_storage_date()
    amount = input("Amount of Produce:")
    tips = input("Storage tip: ")

    pantry_item = {
        "produce:": produce,
        "storage_method:": storage_method,
        "storage_date:": storage_date,
        "amount:": amount,
        "tips:": tips
    }

    auth.users[username]["pantry"].append(pantry_item)
    auth.save_users()

    print(f"{produce} has been added to your pantry!")



def view_pantry(username):
    auth.load_users()
    pantry = auth.users[username]["pantry"]

    print("---------- My Pantry -----------------")

    if len(pantry) == 0:
        print("your have nothing in your pantry.")
        return

    for i in range(len(pantry)):
        print(f"Pantry Item {i + 1}")
        print(f"Produce: {pantry[i]['produce']}")
        print(f"Storage Method: {pantry[i]['storage_method']}")
        print(f"Storage_date: {pantry[i]['storage_date']}")
        print(f"Quantity of Item: {pantry[i]['amount']}")
        print(f"Tip for taking care of produce: {pantry[i]['tips']}")




def pantry_menu(username):
    while True:
        print("------- My Pantry ---------")
        print("1.) Add Pantry Item")
        print("2.) View Pantry")
        print("3.) Return Home")
        

        choice = input("Select option: ")

        if choice == "1":
            add_to_pantry(username)

        elif choice == "2":
            view_pantry(username)

            
        elif choice == "3":
            return home

            

        else:
            print("Invalid selection")






