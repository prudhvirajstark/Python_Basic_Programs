#2. Write a program wc.py that takes filename as argument and counts number of lines, words and chars in file.
import sys
num_words=0;
line_count=0;
charcter=0
with open(sys.argv[1],'r') as f:
	for line in f:
		words=line.split()
		line_count=line_count+1
		num_words+=len(words)
		charcter+=sum(len(word)for word in words)
print("No. of words : ",num_words,line_count,charcter)