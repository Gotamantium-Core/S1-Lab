# Module to define function to find fibonacci nums and import it in another module

def fibonacci(n):
    nextNum = 0
    nums = [0, 1];

    for i in range(n):
        nextNum = nums[-1] + nums[-2];
        nums.append(nextNum)
    
    return nums

print(fibonacci(12))

'''
To run in another file, create a new file in same directory and type:

`from Q24 import fibonacci`

and use as normal
'''