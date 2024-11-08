def power(n):
    return lambda a: a ** n


# Generate dynamically new functions, based on the given arguments
power_of_two = power(n=2)
power_of_three = power(n=3)
power_of_five = power(n=5)

print(power_of_two(a=5))
print(power_of_three(a=5))
print(power_of_five(a=5))
