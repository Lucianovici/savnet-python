def simple_generator():
    print('Processing something heavy ...')
    yield 1
    print('Processing something else ...')
    yield 2
    print('Now it is a joke ...')
    yield 3
    yield 4
    yield 5


# Using the generator
gen = simple_generator()

print('Manual with next')
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# print(next(gen))  # raise StopIteration

print('For loop:')
for i in gen:
    print(i)
