#3.	Python Program to Put Even and Odd elements in a List into Two Different Lists.
a=[]
n=int(input("Enter a number: "))
for i in range(1,n+1):
	b=int(input("Enter an element: "))
	a.append(b)
even=[]
odd=[]
for j in a:
	if(j%2==0):
		even.append(j)
	else:
		odd.append(j)
print("The even list:",even)
print("The odd list:",odd)