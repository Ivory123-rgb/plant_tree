from pages import auth

def get_harvest_date():
    while True:
        harvest_date = input("Enter Harvest Date (yyyy-MM-DD):")

        section_date = harvest_date.split("-")

        if len(section_date) == 3 and all(section.isdigit() for section in section_date):
            return harvest_date

        print("Invalid. Use YYYY-MM-DD format.")






def view_harvest(username):
    auth.load_users()
    plants = auth.users[username]["garden"]

    print("---------- Plants Ready to Harvest -----------------")

    plants_red = []

    for plant in plants:
        if plant["plant_progress"] == "Ready to Harvest":
            plants_red.append(plant)


    if len(plants_red)== 0:
        print("You have no plants ready to harvest.")
        return

    for i in range(len(plants_red)):
        print(f"Plant {i + 1}")
        print(f"Plant: {plants_red[i]['plant_type']}")
        print(f"Growing Space: {plants_red[i]['growing_space']}")


def harvest_menu(username):
    while True:
        print("------- Harvest Menu ---------")
        print("1.) View Plants Ready to Harvest")
        print("2.) Return Home")
        

        choice = input("Select option: ")

        if choice == "1":
            view_harvest(username)


            
        elif choice == "2":
            break

            

        else:
            print("Invalid selection")






