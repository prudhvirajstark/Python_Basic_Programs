#20.	Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
string=input("Enter string: ")
string1=input("Enter string1: ")
count=0
count1=0
for i in string:
		count=count+1
for j in string1:
		count1=count1+1
if(count<count1):
	print("Larger string is: ",string1)
elif(count==count1):
	print("Both strings are equal.")
else:
	print("Larger string is: ",string)