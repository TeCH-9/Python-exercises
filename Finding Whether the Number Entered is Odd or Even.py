number = int(input("Enter your number: "))

# First Way

control = "This number is Even" if (number % 2) == 0 else "This number is Odd"
print(control)

# Second Way

if (number % 2) == 0:
    print("Second Way= This number is Even")
else:
    print("Second Way= This number is Odd")
