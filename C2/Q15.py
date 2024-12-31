# Display alternate prime numbers until N (input)
from math import sqrt

def isPrime(n):
    if n == 1: return None
    if n == 0: return None

    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    else:
        return True;


N = int(input("Enter limit: "))

if N == 0 or N == 1:
    print("Set limit higher pls")
    quit()

primes = []
for i in range(2, N):
    # numbers
    if isPrime(i):
        primes.append(i)

print([i for i in primes if primes.index(i)%2==0])