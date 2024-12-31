'''
Use brute force to find the element that appears most frequently in an
array by counting the occurrences of each element and selecting the one
with the highest count. This involves iterating through the array and
maintaining a count for each element.
'''

ls = list(map(int, input("Enter nums: ").split()))
freq = {}

for i in ls:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

keys = [] ; vals = []
for i in freq:
    keys.append(i)
    vals.append(freq[i])

maxval = vals[0]
for i in range(len(vals)):
    if vals[i] > maxval:
        maxval = vals[i]

index = vals.index(maxval)
print(f"{keys[index]} appears {maxval} times")