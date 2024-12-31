# Create, concatenate and print a string. Also access a substring from it

s = input("Enter string: ")

sConcat = input("Enter string to concatenate: ")

print(s+sConcat)

subStr = input("Enter substring to be found: ")

if subStr in s:
    print(subStr, "found in", s)
else:
    print("Substring not found")