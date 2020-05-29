#3.	Python Program to Check if a Given Key Exists in a Dictionary or Not
d1={'A':1,'B':2}
key=input("Enter the key to check: ")
if key in d1.keys():
	print("Key is present and the value of the key is",d1[key])
else:
	print("Key isn't present")