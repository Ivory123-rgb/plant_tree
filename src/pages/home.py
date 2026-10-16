from pages.garden import garden_menu
from pages.pantry import pantry_menu
from pages.recipes import recipes_menu
from pages.harvest import harvest_menu




def home_menu(username):
    while True:
        print("-------------- PlanTree --------------------------------")
        print("1.) Home")
        print("2.) Garden")
        print("3.) Harvest")
        print("4.) Pantry")
        print("5.) Recipes")
        print("6.) Exit")

        choice = input("Select option: ")



        if choice == "1":
            continue

        elif choice == "2":
            garden_menu(username)

        elif choice == "3":
            harvest_menu(username)

        elif choice == "4":
            pantry_menu(username)

        elif choice == "5":
            recipes_menu(username)

        elif choice == "6":
            return

        else:
            print("Invalid selection")





