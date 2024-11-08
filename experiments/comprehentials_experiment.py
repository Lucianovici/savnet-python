fruit_list = ['apple', 'peach', 'banana', 'grapes', 'kiwi', 'pineapple']

count_list = []

for fruit in fruit_list:
    length = len(fruit)
    if length > 5:
        count_list.append(length)

print('Without list comprehensions')
print(count_list)

# List comprehensions - alternative
# Print me every length of fruit for each fruit in fruit_list
print('With list comprehensions')
print([len(fruit) for fruit in fruit_list])

# Print me every length of fruit, if is greater than 5 for each fruit in fruit_list
print([len(fruit) for fruit in fruit_list if len(fruit) > 5])
# [compute_item for item in item_list if condition]
