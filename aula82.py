# Testador de numeros primos
while 1:
	def prime_checker(number):
		flag = 0
		for x in range(2, number): #range(x, y): varre de x a (y-1)
			if number % x == 0:
				flag += 1
		if flag == 0:
			print("Prime number")
			print(flag)
		else:
			print("Not Prime")
			print(flag)
	
	
	n = int(input("Check this number: "))
	prime_checker(number=n)