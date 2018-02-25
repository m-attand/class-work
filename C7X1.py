#C7X1
fname=input('Enter File Name:     ')
fhand=open(fname)
for line in fhand:
	print(line.upper())