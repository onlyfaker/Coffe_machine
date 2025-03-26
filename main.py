from resources import MENU, RESOURCES

def coins_calculator(q, d, n, p, coffee):
    """Calculate total money inserted and check if sufficient for purchase."""
    total_money = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    payback = round(total_money - MENU[coffee]["cost"], 2)

    if payback < 0:
        return 'Not enough money. Money refunded'
    else:
        return f'Here is your change {payback}\n Here is your {coffee} Enjoy!\n'


def check_resources(coffee):
    """Check if machine has sufficient resources for the chosen coffee."""
    for ingredient, required_amount in MENU[coffee]['ingredients'].items():
        if RESOURCES[ingredient] < required_amount:
            print(f'Sorry, not enough {ingredient} in machine')
            return False
    return True


def get_coin_input(coin_type):
    """Safely get coin input from user with error handling."""
    while True:
        try:
            return int(input(f'How many {coin_type} are you inserting? '))
        except ValueError:
            print(f"Invalid input. Please enter a number of {coin_type}.")


def process_order(coffee):
    """Process the entire order for a specific coffee type."""
    if not check_resources(coffee):
        return

    # Prompt for coins with error handling
    quarters = get_coin_input('quarters')
    dimes = get_coin_input('dimes')
    nickles = get_coin_input('nickles')
    pennies = get_coin_input('pennies')

    # Calculate payment and provide result
    payment_result = coins_calculator(quarters, dimes, nickles, pennies, coffee)

    # If payment is successful, update resources
    if payment_result != 'Not enough money. Money refunded':
        for ingredient, required_amount in MENU[coffee]['ingredients'].items():
            RESOURCES[ingredient] -= required_amount
    print(payment_result)

print('    M E N U')
for key, value in MENU.items():
    print(f"{key}: {value['cost']}$")
print()

ongoing = True
while ongoing:
    coffee_choice = input("Choose ('espresso', 'latte', 'cappuccino') or 'report': ").lower()

    if coffee_choice == 'off':#this is a secret mode for maintance to shut the machine completely
        break

    if coffee_choice == 'report':
        print(f"{RESOURCES['water']}ml water\n{RESOURCES['milk']}ml milk\n{RESOURCES['coffee']}g coffee")

    elif coffee_choice in MENU:
        process_order(coffee_choice)
    else:
        print("Invalid choice. Please choose a valid option.")
