# Check if input string is palindrome
s = input("Enter string: ").lower()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")