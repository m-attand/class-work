#exercise 3-3


def gradecomputation(score):
	try:
		if float(score):
			score=float(score)
			if score > 1.00:
				print('Bad Score')
			elif score >= 0.90:
				Grade = 'A'
			elif score >= 0.80:
				Grade = 'B'
			elif score >= 0.70:
				Grade = 'C'
			elif score >= 0.60:
				Grade = 'D'
			else:
				Grade = 'F'
			return Grade
	except:
		print('Bad Score')
score=input('Enter your Score      ')
print('Grade', gradecomputation(score))