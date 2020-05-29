#5.	Python Program to Print Odd Numbers Within a Given Range
lower=int(input("Enter the lower range limit: "))
upper=int(input("Enter the upper range limit: "))
for i in range(lower,upper+1):
	if(i%2==1):
		print(i)