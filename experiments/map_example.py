number_from_input = input('Bagă număr')


# map_of_input = map(lambda range_index: int(number_from_input) ** range_index, range(10))

def power_of(base, exponent):
    return base ** exponent


base_list = [int(number_from_input) for _ in range(10)]  # the base from input, for 10 times
exponent_range = range(9)
map_of_input = map(power_of, base_list, exponent_range)

for i in map_of_input:
    print(i)
