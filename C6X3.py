#C6X3
def count(word, letter2):
	count=0
	for letter in word:
		if letter==letter2:
			count=count+1
	return count

word=input("Enter word     ")
letter=input('Enter letter     ')
userinput=count(word, letter)
print(userinput)

