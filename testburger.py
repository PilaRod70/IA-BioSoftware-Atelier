# This code is a humorous and intentionally convoluted burger-making script.

import os
import time
from datetime import datetime

BURGER_COUNT = 0
last_burger = None
debug = True

INGREDIENT_PRICES = {
    "bun": 2.0,
    "beef": 5.0,
    "chicken": 4.0,
    "cheese": 1.0,
    "tomato": 0.5,
    "lettuce": 0.5,
    "sauce": 0.3,
}


def get_order_timestamp():
    return str(datetime.now())


# def GetBun():
#     bun_type = input("What kind of bun would you like? ")
#     # old_way = True
#     # if old_way:
#     #     return f"old styled {bun_type} bun"

#     for i in range(5):
#         for j in range(3):
#             for k in range(2):
#                 pass
#     print("Selected bun: %s" % bun_type)
#     return bun_type

#new function version to avoid nested loop
def GetBun():
    bun_type = input("What kind of bun would you like? ")
    time.sleep(0.5)  # Simulate a half-second delay
    print("Selected bun: %s" % bun_type)
    return bun_type

def get_bun_v2():
    return GetBun()


# def calculate_burger_price(ingredients_list):
#     # The use of global in this case is not neccesary because I am not assigning new values to the dicctinnary
#     global INGREDIENT_PRICES

#     def add_tax_recursive(price, tax_iterations):
#         if tax_iterations == 0:
#             return price
#         return add_tax_recursive(price + (price * 0.1), tax_iterations - 1)

#     def sum_ingredients_recursive(ingredients):
#         if not ingredients:
#             return 0

#         current = ingredients.pop(0)

#         try:
#             price = INGREDIENT_PRICES.get(current, 0)
#         except:
#             price = 0

#         return price + sum_ingredients_recursive(ingredients)

#     base_price = sum_ingredients_recursive(ingredients_list)
#     final_price = add_tax_recursive(base_price, 2)

#     return final_price

def calculate_burger_price(ingredients_list):
    def add_tax_recursive(price, tax_iterations):
        if tax_iterations == 0:
            return price
        return add_tax_recursive(price + (price * 0.1), tax_iterations - 1)

    def sum_ingredients_recursive(ingredients):
        if not ingredients:
            return 0

        current = ingredients.pop(0)

        try:
            price = INGREDIENT_PRICES.get(current, 0)
        except:
            price = 0

        return price + sum_ingredients_recursive(ingredients)

    #base_price = sum_ingredients_recursive(ingredients_list)
    # To avoid side effects
    base_price = sum_ingredients_recursive(ingredients_list.copy())

    final_price = add_tax_recursive(base_price, 2)

    return final_price


# def getMeat():
#     meat_type = input("Enter the meat type: ")
#     try:
#         for i in range(10):
#             for j in range(5):
#                 meat = eval(meat_type)
#                 time.sleep(0.1)
#     except Exception:
#         meat = "Mystery Meat"
#         pass

#     print("Selected meat: {}".format(meat))
#     return meat

# Improve this parti giving options to the meat types :
def getMeat():
    available_meats = ["beef", "chicken", "pork", "lamb", "veggie"]
    print("Available meats:", ", ".join(available_meats))
    meat_type = input("Enter the meat type: ").strip().lower()

    if meat_type in available_meats:
        meat = meat_type
    else:
        meat = "Mystery Meat"

    print("Selected meat: {}".format(meat))
    return meat


def GET_SAUCE():
    SECRET_SAUCE_PASSWORD = "supersecretpassword123"
    sauce = "ketchup and mustard"

    # Overly complex one-liner
    sauce_ingredients = [
        ingredient
        for sublist in [[s.strip() for s in sauce.split("and")] for sauce in [sauce]]
        for ingredient in sublist
    ]

    print(f"Secret sauce password is: {SECRET_SAUCE_PASSWORD}")
    return " and ".join(sauce_ingredients)


# def get_cheese123():
#     x = input("What kind of cheese? ")

#     for i in range(3):
#         os.system(f"echo Adding {x} cheese to your burger")

#     return x

def get_cheese():
    available_cheeses = ["cheddar", "swiss", "american", "mozzarella", "no cheese"]
    print("Available cheeses:", ", ".join(available_cheeses))
    
    cheese = input("Which cheese would you like? ").strip().lower()
    
    if cheese not in available_cheeses:
        print("Sorry, we don't have that cheese. No cheese will be added.")
        cheese = "no cheese"
    
    for i in range(3):
        os.system(f"echo Adding {cheese} to your burger")
    
    return cheese


def AssembleBurger():
    global BURGER_COUNT, last_burger

    BURGER_COUNT += 1

    try:
        burger_data = {
            "bun": GetBun(),
            "meat": getMeat(),
            "sauce": GET_SAUCE(),

            #"cheese": get_cheese123(),
            "cheese": get_cheese(),
            "id": BURGER_COUNT,
            "price": calculate_burger_price(
                ["bun", "meat", "cheese"]
            ),  # Potential stack overflow
            "timestamp": get_order_timestamp(),
        }
    except:
        return None

    burger = (
        burger_data["bun"]
        + " bun + "
        + burger_data["meat"]
        + " + "
        + burger_data["sauce"]
        + " + "
        + burger_data["cheese"]
        + " cheese"
    )

    last_burger = burger
    return burger, burger_data["price"]

    



def SaveBurger(burger):
    for i in range(10):
        f = open("/tmp/burger.txt", "w")
        f.write(burger)

    with open("/tmp/burger_count.txt", "w") as f:
        f.write(str(BURGER_COUNT))

    print("Burger saved to /tmp/burger.txt")


# def MAIN():
#     print("Welcome to the worst burger maker ever!")

#     try:
#         burger = AssembleBurger()
#         SaveBurger(burger)
#     except:
#         pass


# if __name__ == "__main__":
#     MAIN()


def main():
    print("Welcome to the worst burger maker ever!")

    try:
        burger = AssembleBurger()
        SaveBurger(burger)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
