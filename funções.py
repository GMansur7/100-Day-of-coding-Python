def função (a,b):
	c = a*b
	return c

def funçãob (a,b):
	c = a/b
	return c
a = 0
b = 0
d = 1
loop = True
while loop:	
	if a != d:
		a = int(input("digite um número"))
	e = input("digite uma função: * / + -")
	b = int(input("digite um segundo número"))
	
	if e == "*":
		d = função(a,b)
	elif e == "/":
		d = funçãob(a, b)
				
			
	print(f"{a} {e} {b} = {d}")	
	
	x = input("quer continuar?")
	
	if x == "no":
		loop = False
	else:
		y = input("quer usar o resultado anterior?")
	
		if y == "yes":
			a = d