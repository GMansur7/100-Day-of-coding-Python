import random
from RPS_art import *

user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors."))

pc_choice = int(random.randint(0, 2))

vector = [rock, paper, scissors]

print(f"You choices {vector[user_choice]}")
print(f"Pc choices {vector[pc_choice]}")

if (user_choice == 0) and (pc_choice == 2):
    print("You Win!")
elif user_choice > pc_choice:
    print("You Win!")
elif user_choice == pc_choice:
    print("It's a Draw")
else:
    print("You Lose!")