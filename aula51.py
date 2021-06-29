##################################################################
student_scores = input("Input a list of studet scores").split()
for n in range(0, len(student_scores)):
	student_scores[n] = int(student_scores[n])
print(student_scores)
##################################################################
max = 0
for x in student_scores:
	if x > max:
		max = x 

print("The max score is :", max)