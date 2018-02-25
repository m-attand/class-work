#exercise 4-7


def gradecomputation(score):
	try:
		if float(score):
			score=float(score)
			if score > 1.00:
				print('Bad Score')
			elif score >= 0.9:
				Grade = 'A'
			elif score >= 0.8:
				Grade = 'B'
			elif score >= 0.7:
				Grade =  'C'
			elif score >= 0.6:
				Grade = 'D'
			else:
				Grade = 'F'
			return Grade
	except:
		print('Bad Input')

score = input('Enter your Score      ')
print('Grade', gradecomputation(score))







