##################################################################
student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])
print(student_heights)
##################################################################
max = 0
min = 0
for x in student_heights:
	if x > max:
		max = x
	if x < min:
		min = x
print(max)
print(min)