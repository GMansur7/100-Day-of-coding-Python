def paint_calc(height, widht, cover):
#	cans = round(height * widht / cover, 0) round(numero, numero de significativos)	
	cans = round(height * widht / cover, 0)
	print(f"You need {cans} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Widht od wall: "))
coverage = 5
paint_calc(height=test_h, widht=test_w, cover=coverage)