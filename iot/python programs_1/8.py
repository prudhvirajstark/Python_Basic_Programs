#8.	Python Program to Read a number n and Compute n+nn+nnn.
n=int(input("Enter a number: "))
temp=str(n)
t1=temp+temp
t2=t1+temp
comp=n+int(t1)+int(t2)
print("Tge value is :",comp)