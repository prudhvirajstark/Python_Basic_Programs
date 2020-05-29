#4.	Python Program to check whether two lists are same.
a=[]
n=int(input("Enter a number: "))
for i in range(1,n+1):
	b=int(input("Enter an element: "))
	a.append(b)
c=[]
m=int(input("Enter a number: "))
for i in range(1,m+1):
	d=int(input("Enter an element: "))
	c.append(d)
if(c==a):
	print("Lists are same")
else:
	print("Lists are different")