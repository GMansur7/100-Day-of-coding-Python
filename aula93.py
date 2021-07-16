from replit import clear
#HINT: You can call clear()
import art_aula93
print(art_aula93.logo)
print("Welcome to the secret auction program.")

dicionario = {}
winner = {}
max = 0
	
loop = True	
while loop:

	name = input("What's is your name?: ")
	bid = int(input("What is your bid?: "))
	
	dicionario [name] = bid

	if dicionario[name] > max:
		max = dicionario[name]
		winner = name
		
	x = input("Are any other bidders? Type: 'yes' or 'no': ")
	if x == "no":
		print(f"The winner is {winner} whit a bid of ${max}")
		loop = False
	elif x == "yes":
		clear()
	else:
		print("invalid entry")
		print(f"The winner is {winner} whit a bid of ${max}")
		loop = False