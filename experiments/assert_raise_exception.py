"""
This is how you would fabricate (raise) an exception.
"""
x = 5
y = 6

# This is how you would emulate an `assert`.
# if x != y:
#     raise AssertError('Nasol rau, nu sunt egale!')

assert x == y, 'Nasol rau, nu sunt egale!'

print('Thank you!')
