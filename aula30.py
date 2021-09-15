height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / (height**2), 2)
print(BMI)

if BMI < 18.5:
	print(f"Your BMI is {BMI}, underweight")
elif BMI < 25:
	print(f"Your BMI is {BMI}, normal weight")
elif BMI < 30:
	print(f"Your BMI is {BMI}, overweight")
elif BMI < 35:
	print(f"Your BMI is {BMI}, obese")
else:
	print("clinically obese")