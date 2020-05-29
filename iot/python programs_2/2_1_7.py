#7.	Python Program to Remove the Given Key from a Dictionary
d1={'A':1,'B':3,'C':3}
print("Initial dictionary: ",d1)
key=input("Enter the key to remove: ")
if key in d1.keys():
	del d1[key]
else:
	print("Key isn't present")
	exit(0)
print("Updated dictionary: ",d1)