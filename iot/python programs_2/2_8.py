#8.	Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number.
a=int(input("Enter a Lower number: "))
b=int(input("Enter a Higher number: "))
y=[(x,x**2)for x in range(a,b+1)]
print("List of tuples :"y)