from random import randint


names_string = input ("Give me everybody's names, separeted by a comma. ")
names  = names_string.split(",")
print(names)
name_number = len(names) - 1
random_number = randint(0,name_number)
print(f"{names[random_number]} is goin to buy the today!")