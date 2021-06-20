#print (round(3.1415, 2))
print ("welcome to the tip calculator.")
bill = float (input ("What the total bill? "))
tip = float(input("What percent tip wild you like to give? 10, 12, or 15?"))/100 + 1.00
people =int(input("How many people to split the bil? "))

#result = round( bill/people * tip, 2)
result = "{:.2f}".format(bill/people * tip)
print(f"Each person should pay: $ {result}")