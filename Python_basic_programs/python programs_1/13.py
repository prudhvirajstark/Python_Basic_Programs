#13.	Python Program to print the number of occurrence of a sub string in a given string.
string=input("Enter string: ")
word=input("Enter sub string: ")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
	if(word==a[i]):
		count=count+1
print("Count of the word is: ",count)