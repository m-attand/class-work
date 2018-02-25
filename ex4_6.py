# exercise 4-6
T_hours = input('Total hours worked: ')
T_rate = input('Enter hourly rate: ')
def computepay(hours, rate):
	if hours <=40:
		return rate*hours
	else:
		return(hours-40)*1.5*rate+40*rate
print ('Pay', computepay(int(T_hours), int(T_rate)))