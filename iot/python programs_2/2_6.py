#6.	Python Program to Find the Intersection of Lists.
#7.	Python Program to find union and intersection of lists without repetition.(5 and  6 programs)
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

e=list(set(a)&set(c))
print("Intersection:",e)