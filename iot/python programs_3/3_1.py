#1. Write a program cat.py that takes a filename as command-line argument and prints all the contents of that file.
#python 3_1.py input.txt--command line arguement

import sys
with open(sys.argv[1],'r') as f:
	contents=f.read()
print(contents)