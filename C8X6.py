## C8X6
num_list = []
while True:
	i = input('Enter a number: ')
	if i.lower() == 'done':
		break
	elif not i.isnumeric(): print("Enter a number")
	else:
		num_list.append(int(i))
print("Min: ", min(num_list), "| Max: ", max(num_list))