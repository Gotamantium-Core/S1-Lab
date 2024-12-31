'''
Input two lists from the user. Merge these lists into a third list such that in the merged
list, all even numbers occur first followed by odd numbers. Both the even numbers and
odd numbers should be in sorted order
'''
# sorting the lists according to the Q.
def sortLists(l1, l2):
    oddl = [] ; evenl = []

    for i in l1+l2:
        if i%2 == 0:
            evenl.append(i)
        else:
            oddl.append(i)
        
    oddl.sort() ; evenl.sort()

    return evenl + oddl

list1 = [] ; list2 = []

# Inputting both lists
m = int(input("Enter limit for list one: "))
for i in range(m):
    elem1 = int(input(f"Enter element {i+1}: "))
    list1.append(elem1)

n = int(input("Enter limit for list two: "))
for i in range(n):
    elem2 = int(input(f"Enter element {i+1}: "))
    list2.append(elem2)

print(sortLists(list1, list2))