evenNumbers = []

for i in range(0, 100):
    if (i % 2) == 0:
        evenNumbers.append(i)

print("These are even numbers:", *evenNumbers)
