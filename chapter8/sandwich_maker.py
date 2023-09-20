import pyinputplus, sys

BREAD_CHOICES = {'wheat': 2.50, 'white': 2.25, 'sourdough': 2.05}
PROTEIN_CHOICES = {'chicken': 4.25, 'turkey': 3.15, 'ham': 3.00, 'tofu': 4.00}
CHEESE_CHOICES = {'chedder': 0.25, 'swiss': 0.25, 'mozzarella': 0.50}

def order_sandwiches():
    try:
        bread_cost = BREAD_CHOICES[pyinputplus.inputMenu(list(BREAD_CHOICES.keys()), prompt='Please choose on of the following bread types:\n')]
        protein_cost = PROTEIN_CHOICES[pyinputplus.inputMenu(list(PROTEIN_CHOICES.keys()), prompt='Please choose on of the following protein types:\n')]

        if pyinputplus.inputYesNo(prompt='Do you want cheese on your sandwich?\n') == 'yes':
            cheese_cost = CHEESE_CHOICES[pyinputplus.inputMenu(list(CHEESE_CHOICES.keys()), prompt='Please choose one of the following cheese types:\n')]
        else:
            cheese_cost = 0

        if pyinputplus.inputYesNo(prompt='Do you want mayo, mustard, lettuce, or tomato?\n') == 'yes':
            condiment_cost = 1.25
        else:
            condiment_cost = 0

        sandwich_amount = pyinputplus.inputInt(prompt='How many sandwiches do you want?\n', min=1)
        
        return (bread_cost + protein_cost + cheese_cost + condiment_cost) * sandwich_amount
    
    except KeyboardInterrupt:
        sys.exit()

order_1 = order_sandwiches()
print(f'Your total is ${order_1:.2f}')