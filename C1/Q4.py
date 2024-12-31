# Swap 2 numbers(variables)

a = 12
b = 33

# Using a 3rd variable
temp = b
b = a
a = temp

print(a, b)

#Without a 3rd variable
a = a + b
b = a - b
a = a - b

print(a, b)