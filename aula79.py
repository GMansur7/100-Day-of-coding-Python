def greet(name, location):
	print(f"Hello {name}")
	print(f"How do you do {name}?")
	print(f"Isn't the weather nice today")
	print(f"You location is {location}")

name = input("What is your name?")
location = input("What is your location?")

#greet(name, location)maneira tradicional
greet(location = location, name = name)# Dessa maneira a ordem dos argumentos não importa
