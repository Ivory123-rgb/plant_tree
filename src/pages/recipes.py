from pages import auth

recipes = [
    {
        "recipe_name": "Ratatouille",
        "ingredients": ["zucchini", "eggplant", "bell peppers", "tomatoes", "onions", "garlic", "parsley", "basil", "olive oil"],
        "instructions": ("Saute the onions and garlic at the base of a pan, layer sliced eggplant, zucchini, peppers, and tomatoes on top with a generous amount of olive oil, simmer or bake until tender")
    },

    {
        "recipe_name": "Caprese Salad",
        "ingredients": [ "tomatoes", "mozzarella", "basil", "olive oil", "balsamic glaze"],
        "instructions": ("Slice tomatoes, and layer with mozzarella, basil leaves, olive oil, and balsamic glaze.")
    }
]

def show_recipe(recipe):
    print(f"Recipe: {recipe['recipe_name']}")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Instructions: {recipe['instructions']}")



def find_pantry_item(username):
    auth.load_users()
    pantry = auth.users[username]["pantry"]

    print("-----------Suggested Recipes From Pantry Items ---------------------")

    if len(pantry) == 0:
        print("You must add produce to your pantry to get recipe suggestions.")
        return

    produce_names = []

    for item in pantry:
        produce = item.get("produce", item.get("produce:", ""))
        produce = produce.strip().lower()

        if produce and produce not in produce_names:
            produce_names.append(produce)

    found = False

    for recipe in recipes:
        matching_ingredients = []
        missing_ingredients = []

        for ingredient in recipe["ingredients"]:
            if ingredient in produce_names:
                matching_ingredients.append(ingredient)

            else:
                missing_ingredients.append(ingredient)


        if len(matching_ingredients) > 0:
            show_recipe(recipe)

            print("You have: " + ", ".join(matching_ingredients))

            if len(missing_ingredients) > 0:
                print("These are ingredients that are also needed for this recipe: " + ", ".join(missing_ingredients))

            else:
                print("You have all the ingredients needed to make this recipe!")

                found = True


    if not found:
        print("No recipes match items in your pantry.")

def recipes_menu(username):
    while True:
        print("-----------Recipes------------------")
        print("1.) Recipes Suggestions Using My Pantry Items")
        print("2.) Return Home")

        choice = input("Select option: ")

        if choice == "1":
            find_pantry_item(username)

            
        elif choice == "2":
            return

            

        else:
            print("Invalid selection")






