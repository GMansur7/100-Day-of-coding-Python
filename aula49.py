##################################################################
student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])
print(student_heights)
##################################################################
soma = 0
for x in student_heights:
	soma += x 
media = round(soma/(n + 1))
print(media)