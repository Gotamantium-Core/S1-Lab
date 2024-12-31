# To determine the largest and smallest in a list of n numbers entered by the user and also find the sum

nums = []

n = int(input("Enter number of elements: "))
for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    nums.append(elem);


print(f"Largest num: {max(nums)}\nSmallest num: {min(nums)} \nSum of nums: {sum(nums)}")