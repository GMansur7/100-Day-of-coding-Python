import art_aula36

print(art_aula36.logo)
print("Welcome to Tresure Island\nYour mission is to find the tresure.")

def Game_Over():
    print("Game Over.")

def Win():
    print("You Win!")

choise1 = input("Left or Right?")

if (choise1 == "Left"):
    choise2 = input("Swim or Wait?")
    if (choise2 == "Wait"):
        choise3 = input("Whit door?") 
        if(choise3 == "Yellow"):
            Win()
        elif (choise3 == "Red"):
            Game_Over()
        elif (choise3 == "Blue"):
            Game_Over()
        else:
            print("You chose a door that doesn't exist")
            Game_Over()
    else:
        Game_Over()
else:
    Game_Over()