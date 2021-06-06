#3. Write a program head.py that takes a filename as command-line argument and prints the first 5 lines of it.

import sys
line_count=0
with open(sys.argv[1],'r') as f:
	for line in f:
		if(line_count==0 and line_count<5):
			contents=f.read()
	line_count=line_count+1
print(contents)