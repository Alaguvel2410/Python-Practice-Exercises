def my(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * my(n - 1)


while True:
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Enter a positive number")
        else:
            break
    except ValueError:
        print("Enter a valid number")


result = my(n)
print("Factorial:", result)
