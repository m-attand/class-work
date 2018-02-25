## C10E1

dict={}
tups={}
file = input(' Enter File:     ')
fhand = open(file)
for line in fhand:
    words =line.split()
    if len(words) <3: continue
    if words[0] != 'From': continue
    if words[1] not in dict.keys():
        dict[words[1]]=1
    else:
        dict[words[1]]+=1
for key, value in dict.items():
    tups.pop(value, key)

email = sorted(tups, reverse=True)[0]
print(email[1], email[0])