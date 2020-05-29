#28.	Write a program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc.
import random
for i in range(0,10):
		print(random.randint(i*10+1,i*10+10))