the_list = ['d', '1', 1, 5.5, '1']
other_list = ['a', 'b', '1']

the_list.extend(other_list)
# the_list.append(other_list)  # appends the other list as an item to the_list

print(the_list)
the_list.remove('1')
the_list.remove(1)
print(the_list)


# Experiment with two variables pointing to the same list in memory.
a = [1, 2, 3]
b = a
b.append(55)  # both a and b lists points to the same address.
print(id(a) == id(b))

#
try:
    print(the_list[1])
    print(the_list[101])  # the first exception is raised, and treated below.
    print(the_list[102])
except IndexError as e:
    print('Nasol rau!')
except ValueError as e:
    pass

