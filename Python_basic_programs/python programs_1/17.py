#17.	Python Program to Count the Number of Vowels in a String.
string=input("Enter string: ")
vowels=0
for i in string:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		vowels=vowels+1
print("Number of vowels in the given string: ",vowels)
