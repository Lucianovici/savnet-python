d = {}

try:
    z = d['k']  # throw an exception, that is caught in the `except KeyError`
    p = 1 / 0  # in this case, not executed anymore!
except IndexError as e:
    print('Nasol!')
except ValueError as e:
    print('Nasol!')
except KeyError as e:
    print('Nasol!')

print('Thank you!')
