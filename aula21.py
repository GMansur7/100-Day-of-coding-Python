height = input ("enter your height in m: ")
weight = input("enter your weight in kg: ")

m = float(height)
kg = float(weight)
bmi = (kg / (m **2))

print ("your BMI is: " + str(bmi))