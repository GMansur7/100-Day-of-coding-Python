print("\nWelcome to the Love Calculator!\n")
name1 = input("\nWhats is your name?\n")
name2 = input("\nWhats is their name?\n")

#variable.lower() Is case sensitive
#variable.count()
# campare whit TRUE LOVE
score1 = 0
score2 = 0

score1 += name1.lower().count("t")
score1 += name1.lower().count("r")
score1 += name1.lower().count("u")
score1 += name1.lower().count("e")

score1 += name2.lower().count("t")
score1 += name2.lower().count("r")
score1 += name2.lower().count("u")
score1 += name2.lower().count("e")

score2 += name1.lower().count("l")
score2 += name1.lower().count("o")
score2 += name1.lower().count("v")
score2 += name1.lower().count("e")

score2 += name2.lower().count("l")
score2 += name2.lower().count("o")
score2 += name2.lower().count("v")
score2 += name2.lower().count("e")

result = str(score1) + str(score2)

if int(result) <10 or int(result) > 90:
	print (f"\nYour score is {result}, you go together like coke and mentos.")

elif 40 < int(result) < 50:
	print (f"\nYour score is {result}, you are alright together.")

else:
	print(f"\nYour score is {result}.")
