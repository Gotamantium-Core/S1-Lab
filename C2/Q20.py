n = 4

# Pattern 1
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    
    print()


# Pattern 2
for i in range(n+1):
    for j in range(n-i):
        print(" ", end="")
    
    for j in range(i):
        print("* ", end="")
    
    print()

# Pattern 3
'''for i in range(1, 2*n):
    if i < n: # top half
        stars = "* "*(i)
        spaces = " "*(n-i)
    else:
        stars = "* "*(2*n-i)
        spaces = " "*(i-n)

    print(f"{spaces}{stars}")
'''

for i in range(2*n-1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    
    