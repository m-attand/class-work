## C9E2
dict={}
file = input('Enter File:   ')
fhand = open(file)
for line in fhand:
    words = line.split()
    if len(words)<3:continue
    if words[0] != 'From': continue
    if words[2] not in dict.keys():
        dict[words[2]]=1
    else:
        dict[words[2]]+=1
print(dict)
