##################################################################
student_scores = input("Input a list of studet scores").split()
for n in range(0, len(student_scores)):
	student_scores[n] = int(student_scores[n])
print(student_scores)
##################################################################
soma = 0
for x in student_scores:
	soma += x 
media = round(soma/(n + 1))
print(media)