number = int(input("Enter a number:"))

for i in range (1, number):
    if i%3 == 0 and i%5 == 0:
        print(i)


