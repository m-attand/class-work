## C8X2.py
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    if len(words) < 0: continue
    print(words[2])