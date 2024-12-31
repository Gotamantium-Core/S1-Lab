# Print armstrong numbers in a given range

def isArmstrong(n: int):
    digits = 0
    last = 0
    pSum = 0

    temp = n
    while temp:
        temp //= 10
        digits += 1
    
    temp = n
    while temp:
        last = temp%10
        pSum += last**digits

        temp //= 10
    
    if n == pSum:
        return True
    else: 
        return False;

start = 10
end = 10000

for i in range(start, end+1):
    if isArmstrong(i):
        print(i)