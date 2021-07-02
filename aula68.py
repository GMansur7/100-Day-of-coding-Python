#Hangman project
import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
word_chosen = []
hide_word = []

for x in word:
	word_chosen.append(x)
	hide_word.append("_")
	
#print(word_chosen)
print("You are play the HangMan! \nThe word is: ")
print(hide_word)
lifes = 5
print(f"You have {lifes} lifes")
and_game = False

while not and_game:
	letter = input("Chose a letter: ")
	position = 0
	for position in range(position, len (word)):
		if letter in word_chosen[position]:
			hide_word[position] = letter
			position += 1
	if letter not in word_chosen:
		lifes -= 1

	print(f"You have: {lifes} lifes")
	print(hide_word)
	if "_" not in hide_word:
		and_game = True
		print("You Win!")
	if lifes == 0:
		and_game = True
		print("You Loose!")