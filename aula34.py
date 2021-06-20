print ("Welcome to dthe Rollercoaster!")
height = int(input("Whats is yor height in cm?: "))

if height >= 120:
	print ("You can ride the Rollercoaster!")
	age = int(input("What is your age? "))
	if age < 12:
		bill = 5
		print("Child ticks are $5.")
	elif age <= 18:
		bill = 7
		print("Youth ticketd are $7.")
	elif 45 <= age <=55:
		print("Everything if goin to be ok. Have free ride on US!")
		bill = 0
	else:
		bill = 12
		print("Adult tickets are $12.")

	wants_photo = input("Do you wnat a photo taken? Y or N?. ")
	if wants_photo == "Y":
		bill += 3
	print(f"You final bill is ${bill}")
else:
	print ("Sorry, you hev to grow taller before you can ride")