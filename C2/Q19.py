# Convert celcius to fahrenheit and vice versa
'''
C/5=(F-32)/9

C = 5/9(F-32)

F = 32+(5C/9)
'''



def CtoF(temp):
    return 32 + 9 * temp/5

def FtoC(temp):
    return 5/9 * (temp - 32)

temp = int(input("Enter temperature: "))

print(f"{temp}°C = {CtoF(temp)}°F \n{temp}°F = {FtoC(temp)}°C ")