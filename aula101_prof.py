from replit import clear
from calc_art import logo
print (logo)
def multiply (n1, n2):
	return  n1 * n2
def divide (n1, n2):
	return n1 / n2
def add (n1, n2):
	return n1 + n2
def subtract (n1, n2):
	return n1 - n2
operations = {	
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}
def calculator():
	num1 = float(input("What's the first number?: "))
	for symbol in operations:
		print(symbol)
	loop1 = True
	while loop1:
		operation_symbol = input("Pick an operation: ")
		num2 = float(input("What's the next number?: "))
		answer1 = operations[operation_symbol](num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {answer1}")
		x = input(f"Type 'y' to comtinue calculating with {answer1}, or type 'n' to start a nem calculation: ")
		for symbol in operations:
			print(symbol)
		if x == "y":
			num1 = answer1
		elif x == "n":
			clear()
			loop1 = False
			print (logo)
			calculator()
calculator()