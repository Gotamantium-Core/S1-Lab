# Greatest common divisor using recursion

'''
hcf is the largest num that can divide the two wholly

suppose a = 12, b = 18

hcf is 6 because
factors(12) = [1, 2, 3, 4, 6, 12]
factors(24) = [1, 2, 3, 4, 6, 8, 12, 24]

the largest common number b/w the two is 6
'''

def hcf(m, n):
    if n == 0:
        return m;    
    
    return hcf(n, m%n)
    


print(hcf(100, 15))

'''
hcf(60, 24) => 24 != 0 => hcf(24, 60%24);
and, 
60%24 = 12;

so, 
hcf(24, 12) => 12 != 0 => hcf(12, 24%12);
and, 
24%12 = 0;

so, 
hcf(12, 0) => 12;

then,
hcf(24, 12) => 12;

finally,
hcf(60, 24) => 12;
'''