## C8X4.py
fhand = open('romeo.txt')
words = []
for line in fhand:
    words=line.split()
    for word in words:
        if word not in words:
            words.append(word)
sorted(words)
print(words)