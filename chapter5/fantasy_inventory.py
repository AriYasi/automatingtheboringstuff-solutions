fantasy_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print('Inventory:')

    total_items = 0

    for k, v in inventory.items():
        total_items += v
        print(str(v) + '\t' + k)
    
    print('Total number of items: ' + str(total_items))

def add_to_inventory(inventory, added_items):
    for index, item in enumerate(added_items):
        inventory.setdefault(item, 0)
        inventory[item] += 1

display_inventory(fantasy_inventory)
add_to_inventory(fantasy_inventory, dragon_loot)
display_inventory(fantasy_inventory)