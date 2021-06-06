#10.	A simple substitution cipher is an encryption scheme where each letter in an alphabet to replaced by a different letter in the same alphabet with the restriction that each letter's replacement is unique. The template for this question contains an example of a substitution cipher represented a dictionary CIPHER_DICTIONARY. Your task is to write a function encrypt(phrase,cipher_dict) that takes a string phrase and a dictionary cipher_dict and returns the results of replacing each character in phrase by its corresponding value in cipher_dict.

#		CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}
	
#	encrypt("cat", CIPHER_DICT) should return ”km “
