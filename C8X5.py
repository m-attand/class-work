##C8X5
f1 = input('Enter file: ')
f = open(f1)
count = 0
for line in f:
	words = line.split()
	if len(words) > 3 and words[0] == 'From':
		count+=1
		print(words[1])