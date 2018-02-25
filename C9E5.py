##C9E5

dict={}
file = input(' Enter File:     ')
fhand = open(file)
for line in fhand:
    words =line.split()
    if len(words) <3: continue
    if words[0] != 'From': continue
    address = words[1][words[1].find("@")+1:len(words[1])]
    if address not in dict.keys():
        dict[address]=1
    else:
        dict[address]+=1
print(dict)