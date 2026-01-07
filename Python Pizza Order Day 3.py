print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N? ")
extra_Cheese = input("Do you want extra cheese on your pizza? Y or N? ")
total = 0

if size == "S":
    total = 15
    if pepperoni == 'Y':
        total += 2
        if extra_Cheese == 'Y':
            total += 1
            print("Your total is $" + str(total) + '.')
    
elif size == "M":
    total = 20
    if pepperoni == 'Y':
        total += 3
        if extra_Cheese == 'Y':
            total += 1 
            print("Your total is $" + str(total) + '.')            
else:
    total = 25
    if pepperoni == 'Y':
        total += 3
        if extra_Cheese == 'Y':
            total += 1
            print("Your total is $" + str(total) + '.')            