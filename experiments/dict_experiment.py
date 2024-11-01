# A list of objects (dicts), to process

the_list = [
    {'unit_price': 123.0, 'qty': 22},
    {'unit_price': 111.0, 'qty': 1},
    {'unit_price': 88.0, 'qty': 23},
]

for item_in_the_database in the_list:
    total_price = item_in_the_database['unit_price'] * item_in_the_database['qty']
    item_in_the_database.update({
        'total_price': total_price
    })


def sort_key(item):
    return item['unit_price']


# the_list.sort(key=lambda item: item['unit_price'])
the_list.sort(key=sort_key)

print(the_list)


def extract_unit_price(item):
    return item['unit_price']


unit_price_list = [extract_unit_price(item) for item in the_list]
print('List of unit price values', unit_price_list)
