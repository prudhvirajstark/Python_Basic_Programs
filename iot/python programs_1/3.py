#3.	Python Program to Print all Numbers in a Range Divisible by a Given Number. [ if range is from 1 to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ]
lower=int(input("Enter the lower range limit: "))
upper=int(input("Enter the upper range limit: "))
n=int(input("Enter the number to be divided by: "))
for i in range(lower,upper+1):
	if(i%n==0):
		print(i)