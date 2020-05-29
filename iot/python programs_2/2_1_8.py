#8.	Write a function is_empty(my_dict) that takes a dictionary my_dict and returns True if my_dict is empty and False otherwise.
def is_empty(my_dict):
	if not bool(my_dict):
		print("True")
	else:
		print("False")
	return
my_dict={'A',1}
is_empty(my_dict)

