#7.	Python Program to Find the Smallest Divisor of an Integer.
n=int(input("Enter a number: "))
a=[]
for i in range(2,n+1):
	if(n%i==0):
		a.append(i)
a.sort()
print("Smallest divissor is:",a[0])