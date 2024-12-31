'''
Develop a greedy algorithm to manage traffic flow by optimizing traffic
light timings at intersections.
Example: Intersections with traffic volumes [500 vehicles/hour, 300 vehicles/hour, 400 vehicles/hour, 600 vehicles/hour] would adjust lights in the
order [4, 1, 3, 2].

Ans: 
traffing = [500, 300, 400, 600]
intersects = [1, 2, 3, 4] # intersection numbers

now sort traffings in asc/desc order (depending on requirements)
{example shown is in asc order}
traffing = [300, 400, 500, 600]
intersects = [2, 3, 1, 4]


return intersects as final answer
'''
n = int(input("Enter number of entrances/exits: "))

l = []
for i in range(n):
    e = int(input(f"Enter traffing volumes in {i+1}: "))
    l.append(e)

l = [500, 300, 400, 600, 900, 2300, 200]

indexes = [(i, l.index(i)+1) for i in l]
indexes = sorted(indexes, key=lambda x: x[0], reverse=True)

print([i[1] for i in indexes])

