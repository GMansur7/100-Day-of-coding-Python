print("Welcome to Python Pizza Deliveries!")

size = input("Whats sixe pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N?: ")
extra_cheese = input("Do you wnat extra cheese? Y or N: ")


if size == "S":
	price = 15
elif size == "M":
	price = 20
else:#size == "L" não importa:
	price = 25

# Essa solução executa passos a mais, porém tbm funciona. ;)
#if (add_pepperoni == "Y") and (size == "S"):
#	price += 2
#if (add_pepperoni == "Y") and ((size == "M") or (size == "L")):
#	price += 3

if (add_pepperoni == "Y"):
	if size == "S":
		price += 2
	else:# add_pepperoni igual a M ou L não importa
		price += 3

if extra_cheese == "Y":
	price += 1

print(f"Your final bill is ${price}") 