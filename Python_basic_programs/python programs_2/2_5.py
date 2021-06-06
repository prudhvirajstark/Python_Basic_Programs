#5.	Python Program to Find the Union of Lists.
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

e=list(set(a+c))
print("Union:",e)