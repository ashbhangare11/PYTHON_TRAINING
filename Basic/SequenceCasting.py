a=[1,2,3,4,5]   # List Object
b=(1,2,3,4,5)   # Tuple Object
c="Hello"       # String Object

# list() 
obj=list(c)			# separates each character in the string and builds the list
print("STRING TO LIST:" ,obj)	# ['H', 'e', 'l', 'l', 'o']

obj=list(b)			# The parentheses of tuple are replaced by square brackets
print("TUPLE TO LIST:" ,obj)	# [1, 2, 3, 4, 5]

# tuple() 
obj=tuple(c)			# separates each character from string and builds a tuple of characters
print("STRING TO TUPLE:" ,obj)	# ('H', 'e', 'l', 'l', 'o')

obj=tuple(a)			# square brackets of list are replaced by parentheses.
print("LIST TO TUPLE:" ,obj)	# (1, 2, 3, 4, 5)

# str() 
obj=str(a)			# puts the list inside the quote symbols.
print("LIST TO STRING:" ,obj)	# '[1, 2, 3, 4, 5]'

obj=str(b)			# puts the tuple inside the quote symbols.
print("TUPLE TO STRING:" ,obj)	# '(1, 2, 3, 4, 5)'