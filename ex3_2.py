#ex3_2
# Enter Hours:10
# Enter Rate: nine
# Error, please enter numeric input
RegHours=40
try:
	Thours=int(input('Enter Total Hours:     '))
	if float(Thours):
		Thours = float(Thours)
	else:
		print('Error, please enter a numberic input')
	Trate=int(input('Enter Your Hourly Pay Rate:     '))
	if float(Trate):
		Trate = float(Trate)
	else:
		print('Error, please enter a numeric input')
	if Thours>RegHours:
		paycomputation=((Thours-RegHours)*.5*Trate)+(Thours*Trate)
	else: 
		paycomputation=Thours*Trate
	print(paycomputation)
except ValueError:
		print('Error, please enter a numeric input')