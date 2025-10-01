#NUMBER DATA TYPE
var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type
print("NUMBER DATATYPE:")
print("The type of variable having value", var1, " is ", type(var1)) 
print("The type of variable having value", var2, " is ", type(var2)) 
print("The type of variable having value", var3, " is ", type(var3)) 
print("The type of variable having value", var4, " is ", type(var4)) 

# STRING DATA TYPE
str1 = 'Hello World!'
str2 = "Tutorials"
str3 = '''TutorialsPoint'''
print("\n STRING DATATYPE:")
print("The type of variable having value", str1, " is ", type(str1))
print (str1)          # Prints complete string
print (str2)
print (str3)
print (str1[0])       # Prints first character of the string
print (str1[2:5])     # Prints characters starting from 3rd to 5th
print (str1[2:])      # Prints string starting from 3rd character
print (str1 * 2)      # Prints string two times
print (str1 + str2) # Prints concatenated string
print (str1 + " TEST") # Prints concatenated string

# SEQUENCE DATA TYPE
# LIST DATATYPE
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print("\n SEQUENCE : LIST DATATYPE:")
print("The type of variable having value", list, " is ", type(list))
print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

# SEQUENCE DATA TYPE
# TUPLE DATATYPE
tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tuple2 = (['One', 'Two', 'Three'], 1,2.0,3, (1.0, 2.0, 3.0))
tuple3 = 2023, "Python", 3.11, 5+6j, 1.23E-4
tinytuple = (123, 'john')
print("\n SEQUENCE : TUPLE DATATYPE:")
print("The type of variable having value", tuple1, " is ", type(tuple1))
print("The type of variable having value", tuple3, " is ", type(tuple3))
print (tuple1)               # Prints the complete tuple
print (tuple2) 
print (tuple3) 
print (tuple1[0])            # Prints first element of the tuple
print (tuple1[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple1[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple1 + tinytuple)   # Prints concatenated tuples
print (tuple1 + tuple2 + tuple3) 

#update a tuple is not allowed but update a list is allowed
list[2] = 1000		#'List' object support item assignment
print ("\n ", list)

#tuple1[2] = 1000 	#'tuple' object does not support item assignment
#print (tuple1) 	

# SEQUENCE DATA TYPE
# RANGE DATATYPE
print("\n SEQUENCE : RANGE DATATYPE")
print ("\n  Range is:")
for i in range(5):
  print(i)

print ("\n  Range is:")
for i in range(2, 5):
  print(i)

print ("\n Range is:")
for i in range(1, 5, 2):
  print(i)