print ("Welcome to the tip calculator!")
print ("What was the total bill? $")
total_bill = float(input())
print ("What tip percentage will you give? 10, 12, or 15?")
tip = float(input())
tip = tip * 0.01
print ("How many people will split the bill? ")
people = float(input())

tip_bill = total_bill + (total_bill * tip)
split_bill = tip_bill / people
print("Each person should pay: $" + str(split_bill))