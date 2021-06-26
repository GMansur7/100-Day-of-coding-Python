print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
d = 0
a = input("right or left?")
if a == "left" :
	b = input("swim or wait?")
	if b == "wait":
		c = input("red, blue or yellow?")
		if c == "yellow":
			print("You win!")
		elif c == "red":
			print("room of fire, game over")
		elif c == "blue":
			print("ice room, game over")
		else:
			print("you choice a dor that doesn't existe, Game over")
	else:
		print("you are attached by a angry  trout, game over")
else:
	print("you fill into a role, game over")