student_score = {
"Harry" : 81,
"Ron" : 78,
"Hermione" : 99,
"Draco" : 74,
"Neville" : 62}

student_grades = {}

for keys in student_score:
	if student_score[keys] == 100 or student_score[keys] >= 91:
		student_grades[keys] = "Outstanding "
	elif student_score[keys] == 90 or student_score[keys] >= 81:
		student_grades[keys] = "Excceds the expectations"
	elif student_score[keys] ==80 or student_score[keys] >= 71 :
		student_grades[keys] = "Acceptable"
	else: 
		student_grades[keys] = "insufficient"	
				
print (student_grades)	