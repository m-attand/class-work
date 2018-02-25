#3 C9E1
dict = {}
wi = input("Enter a file name")
fi = open(wi)
for line in fi.readlines():
	for word in line.split():
		if word not in dict: dict[word] = 1
print(dict)