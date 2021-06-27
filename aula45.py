import random

while 1:
	choice = int(input("what do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

	rock = '''
	    _______
	---'   ____)
	      (_____)
	      (_____)
 	      (____)
	---.__(___)
	'''
	paper = '''
	    _______
	---'   ____)____
	          ______)
	          _______)
	         _______)
	---.__________)
	'''
	scissors = '''
	    _______
	---'   ____)____
	          ______)
	       __________)
	      (____)
	---.__(___)
	'''

	vector = [rock, paper, scissors]

	pc_choice = random.randint(0, 2)
	
#	print(f"You choice {vector[choice]}")

	if choice >= 3 or choice < 0:
#	if 0 > choice >= 3: # (0 > choice) >= 3
		print("Invalid entry, you lose")
	elif choice == pc_choice:
		print(f"You choice {vector[choice]}")
		print(f"Pc choice {vector[pc_choice]}")
		print("It's a draw!")
	elif choice == 0 and pc_choice == 1:
		print(f"You choice {vector[choice]}")
		print(f"Pc choice {vector[pc_choice]}")
		print("You loose")
	elif choice == 1 and pc_choice == 2:
		print(f"You choice {vector[choice]}")
		print(f"Pc choice {vector[pc_choice]}")
		print("You loose")
	elif choice == 2 and pc_choice == 0:
		print(f"You choice {vector[choice]}")
		print(f"Pc choice {vector[pc_choice]}")
		print("You loose")
	elif choice == 0 and pc_choice == 2:
		print(f"You choice {vector[choice]}")
		print(f"Pc choice {vector[pc_choice]}")
		print("You Win!")
	elif choice == 1 and pc_choice == 0:
		print(f"You choice {vector[choice]}")
		print(f"Pc choice {vector[pc_choice]}")
		print("You Win!")
	elif choice == 2 and pc_choice == 1:
		print(f"You choice {vector[choice]}")
		print(f"Pc choice {vector[pc_choice]}")
		print("You Win!")
	elif choice == 1 and pc_choice == 0:
		print(f"You choice {vector[choice]}")
		print(f"Pc choice {vector[pc_choice]}")
		print("You Win!")
			