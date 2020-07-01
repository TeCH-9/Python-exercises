# First Way

text_0 = input("First Way: Enter what you want: ")

for i in text_0:
    print(i)

# Second Way

text_1 = input("Second Way: Enter what you want: ")

count = 0

while count < len(text_1):
    print(text_1[count:count+1:])
    count += 1
