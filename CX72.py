#CX72
fname=input('Enter File Name:     ')
try:
	fhand=open(fname)
except:
	print('File cannot be opened:', fname)
	exit()

count=0
num=0
for line in fhand:
	line = line.rstrip()
	if line.find('X-DSPAM-Confidence:')==0:
		count=count+1
		num=num+float(line[line.find(':')+1:len(line)])

avg=count/num
print('The average spam confidence:', avg)
