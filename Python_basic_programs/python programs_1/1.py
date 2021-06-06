#1.	Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable.
a=int(input("Enter the value of first number(a): "))
b=int(input("Enter the value of second number(b) : "))
a=a+b
b=a-b
a=a-b
print("a is:",a,"b is:",b)