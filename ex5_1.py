#ex5_1
score = []
while  True:
	try:
		score = input('Enter a number:     ')
		if score.strip() == 'done':
			break
		elif float(score):
			score.append(float(score))
		else:
			print('error')
	except:
		print('error')
if len(score) > 0:
	print('total: %d, Count: %d, Average: %f' % (sum(score),
		len(score),(sum(score/len(score))))