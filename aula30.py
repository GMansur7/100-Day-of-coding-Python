height = input ("enter your height in m: ")
weight = input("enter your weight in kg: ")

m = float(height)
kg = float(weight)
bmi = (kg / (m **2))

print ("your BMI is: " + str("{:.2f}".format(bmi)))

if bmi <= 18.5:
	print("You are underweight")
elif 18.5 <= bmi <= 25.0:
	print("You are Normal")
elif 25.0 <= bmi <= 30.0:
	print("You are overweight")
else:
	print(" Cê tá gordo pacas em bixo")
	
ideal_weight ="{:.2f}".format((m**2) * 25)
print("Seu peso ideal é: ", ideal_weight)