import main

turning_off = 'on'
pofit = 0
resources = {
    "water": 300,
    "milk": 100,
    "coffee": 24
}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            'milk': 0
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
def is_resource_sufficient(order_ingredient):
    """
    returns true if order requirements are fulfilled
    :param order_ingredient:
    :return:
    """
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coin():
    """
    Retruns the total amount of coin
    :return:
    """
    print("please insert coin")
    total = int(input("how many of quarters?: "))*0.25
    total += int(input("how many of dimes?: ")) * 0.1
    total += int(input("how many of nickles?: ")) * 0.05
    total += int(input("how many of pennies?: ")) * 0.01
    return total
def is_transaction_successful(money_received,drink_cost):
    """
    this returns true if transaction was successful or return false if the money is insufficient
    :param money_received:
    :param drink_cost:
    :return:
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        global pofit
        pofit += money_received
        print(f'Here is {change} dollars change')
        return True
    else:
        print("Sorry there is not enough money! Money refunded.")
        return False
def make_coffee(drink_name,order_ingredients):
    """
    deduct the required ingredients from the resouces
    :param drink_name:
    :param order_ingredients:
    :return:
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your coffee {drink_name}☕")
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(
            f"Water:{resources['water']}ml\nMilk:{resources['milk']},l\nCoffee:{resources['coffee']}ml\nMoney:${pofit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coin()
            is_transaction_successful(payment,drink["cost"])

