from pages import auth

def get_location():
    while True: 
        print("Growing Space Location")
        print("1.) Indoors")
        print("2.) Backyard")
        print("3.) Patio")
        print("4.) Window")
        print("5.) Porch")
        print("6.) Balcony")
        print("7.) Other")
  
        choice = input("Select option: ")

        if choice == "1":
            return "Indoors"

        elif choice == "2":
            return "Backyard"

        elif choice == "3":
            return "Patio"

        elif choice == "4":
            return "Window"

        elif choice == "5":
            return "Porch"

        elif choice == "6":
            return "Balcony"

        elif choice == "7":
            return input("Enter the location: ")

        else:
            print("Invalid selection")



def add_grow_space(username):
    auth.load_users()

   
    grow_name = input("Growing space name: : ")
    location = get_location()
    sunlight = get_sunlight_hrs("")
    container_size = input("What is the container type that you will be growing your plant in: ")


    growing_space = {
        "grow_name:": grow_name,
        "location:": location,
        "sunlight:": sunlight,
        "container_size:": container_size
    }

    auth.users[username]["growing_spaces"].append(growing_space)
    auth.save_users()

    print("Growing space has been saved!")



def view_growing_spaces(username):
    auth.load_users()
    spaces = auth.users[username]["growing_spaces"]

    print("----------- Your Growing Spaces")

    if len(spaces) == 0:
        print("You have no growing spaces saved.")
        return

    for i in range(len(spaces)):
        print(f"{i + 1}, {spaces[i]['name']}")
        print(f"Location: {spaces[i]['location']}")
        print(f"Sunlight: {spaces[i]['sunlight']} hours")
        print(f"Container: {spaces[i]['container']}")

def grow_spac_menu():
    while True:
        print("------- Growing Spaces ---------")
        print("1.) Add Growing Space")
        print("2.) View Growing Spaces")
        print("3.) Return Home")
        

        choice = input("Select option: ")

        if choice == "1":
            add_grow_space(username)

        elif choice == "2":
            view_growing_spaces(username)

            
        elif choice == "3":
            return home

            

        else:
            print("Invalid selection")






