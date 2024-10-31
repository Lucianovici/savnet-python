"""
Cap3 Lab1
Exercise 3 - adapted a bit to demonstrate the power of dictionary as hashmap or lookup table.
Example of how a dictionary can be used to quickly and efficiently get a menu item information, based on option key.
"""

coffee_machine_dict = {
    'cappuccino': {
        'title': 'Cappuccino Special',
        'price': 4.0,
    },
    'flat_white': {
        'title': 'Flat White',
        'price': 4.5,
    },
    'espresso': {
        'title': 'Espresso Simple',
        'price': 3.5,
    }
}

# Print menu! Loop through all dictionary items.
for key, value in coffee_machine_dict.items():
    title = value['title']
    price = value['price']
    print(f'Key:{key}: {title} ... {price}')

# Option 0: Infinite loop. Get the option key from input, and only break the loop if the key exists in the pool of keys.
while True:
    option_key = input('What coffee do you want today? (by dict key)')
    if option_key in coffee_machine_dict.keys():
        break

    print('Try again ')

cash = input('Cash In 5 or 10')

# Option1: Exit if no option key is found
# if option_key not in coffee_machine_dict.keys():
#     print('Menu item not existent!')
#     exit('Wrong option!')

# Option 2: Use the espresso option, if invalid option key given from keyboard input
# desired_coffee = coffee_machine_dict.get(option_key, coffee_machine_dict['espresso'])

# Option 3: Treat the KeyError exception for invalid option key and print the error message.
try:
    desired_coffee = coffee_machine_dict[option_key]
    change = int(cash) - desired_coffee['price']
    print(f'Change: {change}')
    print(f"Delivery of product: {desired_coffee['title']}")
except KeyError as e:
    print('Wrong option! ', str(e))

print('Thank you!')
