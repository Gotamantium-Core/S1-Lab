'''
You are given the task of calculating the electricity bill of a house. Each
house has the following components: fan, light, washing machine, and
computer. Each fan consumes 1 unit per day, and each light consumes 0.5
units per day, the washing machine consumes 2 units per day and each
computer consumes 3 units per day. Let the cost of 1 unit be 50 rupees.
Input the number of fans, lights, washing machines, and computers for
a particular house and find the total electricity bill for that house for 2
months. Assume a 30-day month
'''

fans = int(input("Enter number of fans: "))
lights = int(input("Enter number of lights: "))
washingMachines = int(input("Enter number of washing machines: "))
computers = int(input("Enter number of computers: "))

units = 3*fans + 0.5*lights + 2*washingMachines + 3*computers

cost = units * 50 * 30 * 2

print(f"Total costs: Rs {cost}")
