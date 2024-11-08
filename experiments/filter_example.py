length = input('Length: ')

even_numbers = filter(lambda i: i % 2 == 0, range(int(length)))

print(even_numbers)  # it is a filter object = Iterable.

for even_number in even_numbers:
    print(even_number)

print(list(even_numbers))  # reason why empty list = iterator is depleted
