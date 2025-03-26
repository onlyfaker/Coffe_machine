# Coffee Machine Simulator 🍵☕

A command-line simulation of a coffee vending machine that allows users to order espresso, latte, or cappuccino while managing resources and processing payments.

## 🎯 Project Overview

This Python-based Coffee Machine Simulator provides an interactive experience of ordering coffee, managing machine resources, and processing coin payments. It demonstrates object-oriented programming concepts, input validation, and resource management.

## ✨ Features

### 1. Drink Selection
- Choose from three coffee types:
  - Espresso
  - Latte
  - Cappuccino

### 2. Resource Management
- Real-time tracking of machine resources:
  - Water
  - Milk
  - Coffee

### 3. Payment Processing
- Accept multiple coin denominations:
  - Quarters ($0.25)
  - Dimes ($0.10)
  - Nickels ($0.05)
  - Pennies ($0.01)

### 4. Additional Functionalities
- Generate resource reports
- Error handling for invalid inputs
- Automatic resource deduction after successful orders

## 🛠 Requirements

- Python 3.x
- `resources.py` module (containing `MENU` and `RESOURCES` dictionaries)

## 📋 Program Workflow

1. Display available coffee menu with prices
2. Prompt user to select a drink or view report
3. Check resource availability
4. Process coin payment
5. Dispense drink and update resources
6. Provide change if applicable

## 🎮 How to Use

### Starting the Program
```bash
python coffee_machine.py
```

### Menu Options
- Enter `espresso`, `latte`, or `cappuccino` to order
- Enter `report` to view current machine resources
- Enter `off` to exit the program

### Ordering Process
1. Select a drink
2. Insert coins when prompted
3. Receive drink or refund based on payment

## 🔢 Coin Input
- Enter the number of each coin type when prompted
- Machine calculates total payment automatically

## 🚦 Error Handling
- Validates resource availability before order
- Handles invalid coin and menu inputs
- Provides clear error messages

## 📊 Resource Tracking
The machine tracks:
- Water (ml)
- Milk (ml)
- Coffee (g)

## 🧩 Code Structure

### Key Functions
- `coins_calculator()`: Calculate total payment and change
- `check_resources()`: Verify ingredient availability
- `get_coin_input()`: Safe coin input with error handling
- `process_order()`: Manage entire ordering process

## 🔮 Potential Enhancements
- Add more drink options
- Implement admin mode for restocking
- Create persistent resource tracking
- Add logging capabilities

## 📝 Example Interaction
```
    M E N U
espresso: 1.5$
latte: 2.5$
cappuccino: 3.0$

Choose ('espresso', 'latte', 'cappuccino') or 'report': latte
How many quarters are you inserting? 5
How many dimes are you inserting? 2
How many nickles are you inserting? 1
How many pennies are you inserting? 2
Here is your change 0.25
Here is your latte. Enjoy!
```

## 📄 License
MIT License
