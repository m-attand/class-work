#ex3_1
# Enter Hours:45
# Enter Rate: 10
# pay: 475.0
Thours=int(input('Enter Total Hours:     '))
Trate=int(input('Enter Your Hourly Pay Rate:     '))
RegHours=40
if Thours > RegHours:
	paycomputation=((Thours-RegHours)*.5*Trate)+(Thours*Trate)
else: 
	paycomputation=Thours*Trate
print(paycomputation)
	
