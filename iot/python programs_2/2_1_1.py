#1.	Python Program to Add a Key-Value Pair to the Dictionary
key=int(input("Enter a key to be added: "))
value=int(input("Enter a value for the key to be added: "))
d={}
d.update({key:value})
print("Updated dictionary:",d)