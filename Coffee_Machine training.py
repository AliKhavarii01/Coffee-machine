MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] <= resources[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}")
            return False
        
def transaction_successful(money):
    global profit
    if money >= drink["cost"]:
        profit += drink["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

game_over = False

while not game_over:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        game_over = True
    elif order == "report":
        print(f"Water: {resources['water']}ml")#because resources is in a global function
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        if resource_sufficient(drink["ingredients"]):
            quarter = int(input("press your quarters ")) * 0.25
            dime = int(input("press your dimes ")) * 0.10
            nickle = int(input("press your nickles ")) * 0.05
            penny = int(input("press your pennies ")) * 0.01
            money = quarter + dime + nickle + penny
            refund = round(money - drink["cost"], 2)
            order_ingredient = drink["ingredients"]
            if transaction_successful(money):
                print(f"Here is {refund} dollars in change.")
                for item in order_ingredient:
                    resources[item] -= order_ingredient[item]
                print(f"Here is your {order}. Enjoy")
