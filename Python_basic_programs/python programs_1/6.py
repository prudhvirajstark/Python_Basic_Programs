#6.	Python Program to Find the Sum of Digits in a Number.
n=int(input("Enter a number: "))
tot=0
while(n>0):
	dig=n%10
	tot=tot+dig
	n=n//10
print("sum of digits is : ",tot)