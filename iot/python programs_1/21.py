#21.	Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.
string=input("Enter string: ")
count=0
count1=0
for i in string:
		if(i.islower()):
			count=count+1
		elif(i.isupper()):
			count1=count1+1
print("Number of lowercase letters in the given string: ",count)
print("Number of uppercase letters in the given string: ",count1)