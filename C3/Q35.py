'''
Implement a Python function to simulate rolling a six-sided die once. Print
the number rolled.
'''

from random import randint

det = "y"

det = input("Roll? (y/n): ")
while det == "y":
    print(randint(1, 6))
    det = input("Roll again? (y/n): ")

print("Done")   