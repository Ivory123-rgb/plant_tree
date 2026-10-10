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


def get_sunlight_amount():
    while True:
        try:
            sunlight = int(
                input("Hours of sunlight plant recieves each day: ")

                if sunlight >= 0 and sunlight <= 24:
                    return sunlight

                print("Sunlight hours must be between 0 and 24 hrs. ")


        
            )

def add_grow_space(username):
    auth.load_users()

   
    grow_name = input("Growing space:  ")
    location = get_location()
    sunlight = get_sunlight_hrs("")
    container_size = input("What is the container type that you will be growing your plant in: ")


    growing_space = {
        "grow_name": grow_name,
        "location:": location,
        "sunlight:": sunlight,
        "container_size:": container_size
    }

    auth.users[username]["growing_spaces"].append(growing_space)
    auth.save_users()

    print("Growing space has been saved!")



def select_growing_spaces(username):
    auth.load_users()
    spaces = auth.users[username]["growing_spaces"]

    print("----------- Select Growing Spaces")

    if len(spaces) == 0:
        print("You have no growing spaces saved.")
        return

    for i in range(len(spaces)):
        print(f"{i + 1}, {spaces[i]['grow_name']}")
        
    while True:
        try:
            choice = int(input("Select a growing space: "))

            if choice >= 1 and choice <= len(spaces):
                return spaces[choice - 1]

def plant_date():
    while True:
        plant_date = input("Enter Date Planted (yyyy-MM-DD):")

        plant_section_date = storage_date.split("-")

        if len(plant_section_date) == 3 and all(section.isdigit() for section in plant_section_date):
            return storage_date

        print("Invalid. Use YYYY-MM-DD format.")




def get_plant_progress():
     while True: 
        print("---------------- Plant Status ------------------------")
        print("1.) Seed")
        print("2.) Germination/Sprout")
        print("3.) Seedling")
        print("4.) Vegetative Growth")
        print("5.) Budding and Flowering")
        print("6.) Repening / Harvest")
        
  
        choice = input("Select option: ")

        if choice == "1":
            return "Seed"

        elif choice == "2":
            return "Germination/Sprout"

        elif choice == "3":
            return "Seedling"

        elif choice == "4":
            return "Vegetative Growth"

        elif choice == "5":
            return " Budding and Flowering"

        elif choice == "6":
            return "Rady to Harvest"

        else:
            print("Invalid selection")




def add_plant(username):
    auth.load_users()

    selected_space = select_Growing_spaces(username)

    if selected_space is None:
        return


    print("-------------- Add Plant ----------------")
   
    plant_type = input("Plant:  ")
    plant_date = get_plant_date()
    plant_progress = get_plant_progress()
    watering_freq = input("How often does the plant need to be watered?  ")
    notes = input("Plant Notes:")


    plant = {
        "plant_type": plant_type,
        "growing_space": selected_space["grow_name"],
        "plant_date": plant_date,
        "plant_progress": plant_progress,
        "watering_freq": watering_freq,
        "notes": notes
    }

    auth.users[username]["garden"].append(plant)
    auth.save_users()

    print(f"{plant_type} has been added to your garden!")

def view_garden(username):
    auth.load_users()

    spaces = auth.users[username]["growing_spaces"]
    plants = auth.users[username]["garden"]

    print("-------------- My Garden ------------------------")

    if len(spaces) == 0:
        print("No growing spaces available. ")
        return

    for space in spaces:
        print(f"Growing Space: {space['grow_name']}")
        print(f"Location: {space['location']}")
        print(f"Sunlight: {space['sunlight']}")
        print(f"Container Type: {space['container_size']}")

        print("Plants: ")

    for plant in plants:
        if plant["growing_spaces"] == space["grow_name"]:
            print(f"Plant: {plant['plant_type']}")
            print(f"Date Planted: {plant['plant_date']}")
            print(f"Progress: {plant['plant_progress']}")

            print(f"Watering Frequence: {plant['water_freq']}")
            print(f"Plant Notes: {plant['notes']}")

def garden_menu(username):
     while True: 
        print("---------------- My Garden ------------------------")
        print("1.) Add Grow Space")
        print("2.) Add Plant")
        print("3.) View My Garden")
        print("4.) Home")
        
        
  
        choice = input("Select option: ")

        if choice == "1":
            add_grow_space(username)

        elif choice == "2":
            add_plant(username)

        elif choice == "3":
            view_garden(username)

        elif choice == "4":
            break

        

        else:
            print("Invalid selection")

