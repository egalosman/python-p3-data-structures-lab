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
# python data_structures.py
print(spicy_foods[1])

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
    



def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

#print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
   for food in spicy_foods:
       name = food["name"]
       cuisine = food["cuisine"]
       heat_lvl = food["heat_level"]

       heat_emoji_number = "🌶" * heat_lvl 
       print(f"{name} ({cuisine}) | Heat Level: {heat_emoji_number}")


#print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine.capitalize():
            return food

#print(get_spicy_food_by_cuisine(spicy_foods, "thai"))
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
       name = food["name"]
       cuisine = food["cuisine"]
       heat_lvl = food["heat_level"]

       heat_emoji_number = "🌶" * heat_lvl 
       if heat_lvl > 5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_emoji_number}")

def get_average_heat_level(spicy_foods):
    avg_heat_lvl = [food["heat_level"] for food in spicy_foods]
    print(avg_heat_lvl)
    sum = 0
    for x in avg_heat_lvl:
        sum += x
        avg = sum / 3
    
    return avg

print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    
    spicy_foods.append(spicy_food)
    return spicy_foods

create_spicy_food(spicy_foods, spicy_food =[{
        "name": "Malawah",
        "cuisine": "Somali",
        "heat_level": 1,
    }]) 