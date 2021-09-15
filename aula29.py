altura = int(input("Qual é a sua altura?"))
if altura >= 120:
	print("Você pode andar na montamha Russa!")
	idade = int(input("Qual é a sua idade?"))
	if idade < 12 :
		print("Seu ingreço custa $5.")
	elif idade < 18:
		print("Seu ingreço custa $7.")
	else:
		print("Seu ingreço custa $12.")
else:
	print("Desculpe, você precisa ter no minimo 120 cm de altura")
