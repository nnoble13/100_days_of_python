from menu import MENU, resources


#TODO 1: User prompt for input
def user_prompt():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    return user_choice

def resources_available(order_ingredients):
    enough_resources = True
    for thing in order_ingredients:
        if order_ingredients[thing] >= resources[thing]:
            print(f"Sorry there is not enough {thing}.")
            return False
    return enough_resources

#TODO 1.1: Prompt shows after every action
profit = 0
machine_on = True


while machine_on:
    user_choice = user_prompt()

#TODO 2: Turn OFF coffee machine using secret word, possibly with 1
    if user_choice == "off":
        machine_on = False

#TODO 3: Print report showing current resources values
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: €{profit}")
    else:
        drink = (MENU[user_choice])
        if resources_available(drink["ingredients"])


#TODO 4: Check if resources are sufficient for the drink order


#TODO 5: Process coins
#TODO 6: Check if transaction is successful
#TODO 6.1: Check if user has inserted enough money
#TODO 6.2: Check if user has inserted too much money, give change
#TODO 7: Make coffee
