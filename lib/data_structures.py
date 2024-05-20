spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_list = [n["name"] for n in spicy_foods]
    return spicy_list

def get_spiciest_foods(spicy_foods):
    spiciest_list = [n for n in spicy_foods if n["heat_level"] > 5]
    return spiciest_list

def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
        print(f'{n["name"]} ({n["cuisine"]}) | Heat Level: {"🌶" * n["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_cuisine = [n for n in spicy_foods if n["cuisine"] == cuisine]
    return spicy_cuisine[0]

def print_spiciest_foods(spicy_foods):
    for n in spicy_foods:
        if n["heat_level"] > 5:
            print(f'{n["name"]} ({n["cuisine"]}) | Heat Level: {"🌶" * n["heat_level"]}')

def get_average_heat_level(spicy_foods):
    list_length = len(spicy_foods)
    heat_total = 0
    for n in spicy_foods:
        heat_total = heat_total + n["heat_level"]
    return heat_total / list_length

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
