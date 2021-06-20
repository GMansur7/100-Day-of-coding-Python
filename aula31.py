#ano bissexto 
loop = 0
while loop <= 9:
	loop += 1
	year = int(input("whit year do you want to check?"))
	flag =0
	if year % 4 == 0:
		if year % 100 != 0:
			if year % 400 != 0:
				print("The year is leap")
				flag = 1 
	if flag == 0:
		print("The year is not leap")
