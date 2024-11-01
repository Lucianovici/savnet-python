the_list = ['xxx', 'yyy', 'zzz']

the_dict = {'x': 1, 'y': 2}
the_string = 'ceva'

values = [str(v) for v in the_dict.values()]
new_list = '~~~'.join(values)

print(new_list)
