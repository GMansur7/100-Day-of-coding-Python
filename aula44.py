row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]
map = [row1, row2, row3]

#map[1][2] = 1
print(f"{row1}\n{row2}\n{row3}")
position = input("onde quer quardar a informação? xy:")#Usar .split(", ") caso utilize ", " como separador

x = int(position[0])
y = int(position[1])
map[y -1][x -1] = "x"

print(f"{row1}\n{row2}\n{row3}")
