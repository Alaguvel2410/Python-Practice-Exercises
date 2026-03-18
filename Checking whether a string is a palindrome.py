a = input("Enter a string value: ").replace(" ", "").lower()
if a == a[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
