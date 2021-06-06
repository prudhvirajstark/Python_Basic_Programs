#1.	Python Program to Find the Largest Number in a List
a=[]
n=int(input("Enter a number: "))
for i in range(1,n+1):
	b=int(input("Enter an element: "))
	a.append(b)
a.sort()
print("Largest element is : ",a[n-1])