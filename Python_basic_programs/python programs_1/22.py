#22.	Python Program to Calculate the Number of Digits and Letters in a String.
string=input("Enter string: ")
count=0
count1=0
for i in string:
		if(i.isalpha()):
			count=count+1
		elif(i.isnumeric()):
			count1=count1+1
print("Number of letters in the given string: ",count)
print("Number of digits in the given string: ",count1)