#4.	Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n=int(input("Enter a number: "))
d={x:x*x for x in range(1,n+1)}
print(d)