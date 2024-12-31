# Recursive function to add two numbers


def add(m,n):
    if n == 0:
        return m;

    y = add(m,n-1)+1;
    
    return y;
print(add(5, 4))

'''
add(5, 4) => y = add(5, 3) + 1;

so, 
add(5, 3) => y = add(5, 2) + 1;

so, 
add(5, 1) => y = add(5, 1) + 1;

so, 
add(5, 0) => 5;

then, 
add(5, 1) => y = 5+1;

then, 
add(5, 2) => y = 6+1;

then, 
add(5, 3) => y = 7+1;

then, 
add(5, 4) => y = 8+1;

finally, 
add(5, 4) => 9

'''