import random


def raise_to_power_of(base, power):
    return base ** power


print(raise_to_power_of(2, 3))
print((lambda base, power: base ** power)(2, 3))

random_list_of_numbers = [{'x': random.randint(0, 100)} for _ in range(100)]

print(random_list_of_numbers)
print(sorted(random_list_of_numbers, key=lambda i: i['x']))
