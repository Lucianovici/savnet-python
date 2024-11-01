import random

# the_list = []
# for _ in range(100):
#     the_list.append(random.randint(0, 100))

random_int_list = [random.randint(0, 100) for _ in range(100)]
the_list = [i for i in range(101)]

print(random_int_list)
print(the_list)
