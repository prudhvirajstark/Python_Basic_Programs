#9.	Python Program to Remove the Duplicate Items from a List.
a=[]
n=int(input("Enter a number: "))
for i in range(1,n+1):
	b=int(input("Enter an element: "))
	a.append(b)
print("List without duplicates:",set(a))