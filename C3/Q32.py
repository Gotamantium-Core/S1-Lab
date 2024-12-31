'''
Apply dynamic programming to determine the number of ways to climb
a staircase with n steps, where you can take 1 or 2 steps at a time. This
method builds solutions incrementally by storing the number of ways to
reach each step.
'''

def climb(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    ways = [1, 1]
    for i in range(2, n+1):
        ways.append(ways[i-1]+ways[i-2])
    
    return ways, ways[-1]

print(climb(6))
