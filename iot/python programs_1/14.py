#14.	Python program to print the lowest index in the string where substring sub is found within the string.
string=input("Enter string: ")
word=input("Enter sub string: ")
result=string.find(word)
print(word,"is found at index",result)