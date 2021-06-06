#10.	Python Program to Read a List of Words and Return the Length of the Longest One.
a=[]
n=int(input("Enter a number: "))
for i in range(0,n):
	b=int(input("Enter an element: "))
	a.append(b)
temp=a[0]
for i in a:
	if(i>temp):
		temp=i
print("Word with longest length:",temp)