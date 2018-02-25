##C10E2
dict={}
tups={}
file = input(' Enter File:     ')
fhand = open(file)
for line in fhand:
    words =line.split()
    if len(words) <3: continue
    if words[0] != 'From': continue
    hour=words[5].split(':')[0]
    if hour not in dict.keys():
        dict[hour]=1
    else:
        dict[hour]+=1
for key, value in dict.items():
    tups.append((key, value))
total=sorted(tups)
for hr in total:
    print(hr[0], hr[1])

