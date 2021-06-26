import random

while 1:
	text = (input("what do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#	if text 

	choise = int(text)
	vector = ["Pedra", "Papel", "Tesoura"]

	pc_choise = random.randint(0, 2)
	
#	print(f"vc escolheu {vector[choise]}")

	if choise >= 3 or choise < 0:
#	if 0 > choise >= 3:
		print("entrada invalida, vc perdeu")
	elif choise == pc_choise:
		print(f"vc escolheu {vector[choise]}")
		print(f"Pc choise {vector[pc_choise]}")
		print("Empate ")
	elif choise == 0 and pc_choise == 1:
		print(f"vc escolheu {vector[choise]}")
		print(f"Pc choise {vector[pc_choise]}")
		print("You loose")
	elif choise == 1 and pc_choise == 2:
		print(f"vc escolheu {vector[choise]}")
		print(f"Pc choise {vector[pc_choise]}")
		print("You loose")
	elif choise == 2 and pc_choise == 0:
		print(f"vc escolheu {vector[choise]}")
		print(f"Pc choise {vector[pc_choise]}")
		print("You loose")
	elif choise == 0 and pc_choise == 2:
		print(f"vc escolheu {vector[choise]}")
		print(f"Pc choise {vector[pc_choise]}")
		print("You Win!")
	elif choise == 1 and pc_choise == 0:
		print(f"vc escolheu {vector[choise]}")
		print(f"Pc choise {vector[pc_choise]}")
		print("You Win!")
	elif choise == 2 and pc_choise == 1:
		print(f"vc escolheu {vector[choise]}")
		print(f"Pc choise {vector[pc_choise]}")
		print("You Win!")
	elif choise == 1 and pc_choise == 0:
		print(f"vc escolheu {vector[choise]}")
		print(f"Pc choise {vector[pc_choise]}")
		print("You Win!")
			