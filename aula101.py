from replit import clear
from calc_art import logo
print (logo)
def multiplicação (a, b):
	return  a * b
def divisão (a, b):
	return a / b
def soma (a, b):
	return a + b
def subtração (a, b):
	return a - b
a = 0
b = 0
d = 1
loop = True
while loop:	
	if a != d:
		a = float(input("What's the first number?: "))
	operador = input("Pick an operation: \n *\n /\n +\n -\n")
	b = float(input("What's the next number?: "))
	if operador == "*":
		d = multiplicação (a, b)
	elif operador == "/":
		d = divisão (a, b)
	elif operador == "+":
		d = soma (a, b)
	elif operador == "-":
		d = subtração (a, b)
	else:
		print ("Invalid operation")				
	print(f"{a} {operador} {b} = {d}")
	x = input(f"Type 'y' to comtinue calculating with {d}, or type 'n' to start a nem calculation: ")
	if x == "y":
		a = d
	elif x == "n":
		clear()
		print (logo)