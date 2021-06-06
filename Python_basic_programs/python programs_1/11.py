#11.	Python Program to Count the Number of Digits in a Number.
n=int(input("Enter a number: "))
count=0
while(n>0):
	count=count+1
	n=n//10
print("reverse of the number:",count)