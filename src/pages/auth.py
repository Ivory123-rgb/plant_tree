import json
import os
from pages.home import home_menu

USERS_FILE = "users.txt"

users = {}

def load_users():
    global users

    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = {}


    else:
        users = {}


    for user in users.values():
                user.setdefault("experience_level", "beginner")
                user.setdefault("growing_spaces", [])
                user.setdefault("garden", [])
                user.setdefault("pantry", [])
                user.setdefault("recipes", [])
                user.setdefault("harvest", [])




            

def save_users():
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def get_string(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value


        print("Incorrect input ")


def get_experience_level():
    while True:
        print("Gardening Experience")
        print("1.) Beginner")
        print("2.) Experienced")


        choice = input("Select option: ")

        if choice == "1":
            return "beginner"

        elif choice == "2":
            return "experienced"

        else:
            print("Invalid selection")



def create_account():
    load_users()
    user_id = len(users) + 1

    print("----------------- Create Account ---------------")

    username = get_string("Username: ")

    if username in users:
        print("Username is already taken, choose another one.")
        return

    password = get_string("Password: ")
    first_name = get_string("First Name: ")
    last_name = get_string("Last Name: ")
    experience_level = get_experience_level()


    users[username] = {
        "userID:": user_id,
        "username:": username,
        "password:": password,
        "first_name:": first_name,
        "last_name:": last_name,
        "experience_level:": experience_level,
        "growing_spaces:": [],
        "garden:": [],
        "harvest:": [],
        "pantry:": [],
        "recipes:": [],

    }


    save_users()
    print("Your account has been successfully created!")



def login():
    load_users()

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Welcome, {users[username]['first_name']}")
        return username


def start_auth_page():
    while True:
        print("------- PLANTREE ---------")
        print("1.) Create Account")
        print("2.) Login")

        choice = input("Select option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            username = login()

            if username:
                home_menu(username)

        else:
            print("Invalid selection")



