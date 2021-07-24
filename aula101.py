#import calc_art
#print(calc_art.logo)
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
		a = float(input("digite um número"))
	operador = input("digite uma função: * / + -")
	b = float(input("digite um segundo número"))
	
	if operador == "*":
		d = multiplicação (a, b)
	elif operador == "/":
		d = divisão (a, b)
	elif operador == "+":
		d = soma (a, b)
	elif operador == "-":
		d = subtração (a, b)
	else:
		print ("Operação inválida")
				
			
	print(f"{a} {operador} {b} = {d}")	
	
	x = input("quer continuar?")
	
	if x == "no":
		loop = False
	else:
		y = input("quer usar o resultado anterior?")
	
		if y == "yes":
			a = d