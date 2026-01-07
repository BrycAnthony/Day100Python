print("Welcome to the rollercoaster!")
Height = int(input("How many cenimeters tall are you? "))
Bill = 0

if Height >= 120:
    Age = int(input("How tall old are you? "))

    if Age < 12:
        print("Child tickets are $5.")
        Bill = 5
    elif Age < 18:
        print("Youth tickets are $7.")
        Bill = 7
    else:
        print("Adult tickets are $12.")
        Bill = 12
    
    Photo = input("Do you want a photo taken? Type Y for yes, and N for no. ")
    if Photo == 'Y':
        Bill += 3
    print("Your final bill is $" + str(Bill) + '.')
else:
    print("Sorry, you are too short to ride.")