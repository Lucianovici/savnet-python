s = 'xxxasdTimiTimixxxTim'

str_to_cut = 'Tim'
chars_to_cut_len = len(str_to_cut)

# remove just the prefix, if any
# print(s.removeprefix(str_to_cut))

# remove all occurrences of the substr.
print(s.replace(str_to_cut, ''))

# inefficient way to remove a substr from a string
index_found = 0
iteration = 0
while index_found >= 0:
    if iteration == 2:
        break

    index_found = s.find(str_to_cut)
    if index_found >= 0:
        s = s[:index_found] + s[index_found + chars_to_cut_len:]

    iteration += 1
print(s)


