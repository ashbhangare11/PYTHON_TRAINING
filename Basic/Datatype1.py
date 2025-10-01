# Using bytes() function to create bytes
print("BYTES() DECIMAL EXAMPLE:")
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)  
print(type(b1))

print("BYTES() HEXA-DECIMAL EXAMPLE:") 
b4 = bytes([0x41, 0x42, 0x43, 0x44, 0x45])  
print(b4)  

print("BYTES() PREFIX 'b' EXAMPLE:")
b2 = b'Hello'  
print(b2)  

print("BYTES() PREFIX 'b' HEXA-DECIMAL EXAMPLE:") 
b3 = b"\x41\x42\x43\x44\x45"
print(b3) 

# Creating a bytearray 
print("\nBYTEARRAY EXAMPLE BY PASSING ITERABLE INTEGER:")
value = bytearray([72, 101, 108, 108, 111])  
print(value)  

print("BYTEARRAY EXAMPLE BY USING UTF-8 ENCODING:")
val = bytearray("Hello", 'utf-8')  
print(val)  

#MEMORYVIEW DATATYPE
print("\nMEMORYVIEW EXAMPLE BY MEMORYVIEW() CONSTRUCTOR:")
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)

print("MEMORYVIEW EXAMPLE BY BUFFER INTERFACE:")
import array
arr = array.array('i', [1, 2, 3, 4, 5])
view = memoryview(arr)
print(view)

print("MEMORYVIEW EXAMPLE BY SLICING BYTE OBJECT:")
data = b'Hello, world!'
# Creating a view of the last part of the data
view1 = memoryview(data[7:])  
print(view1)

print("\nDICTIONARY EXAMPLE:")
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
print (dict.keys())   
print (dict.values())
print (tinydict['name'])

print("\nSET DATATYPE:")
set1 = {123, 452, 5, 6}
set2 = {'Java', 'Python', 'JavaScript'}
print(set1)
print(type(set1))
print(set2)
print(type(set2))

#If you try to put a list or a dictionary in the set collection, Python raises a TypeError(unhashable type).
#set3 = {['One', 'Two', 'Three'], 1,2,3, (1.0, 2.0, 3.0)}
#print(set3)

print("\nBOOLEAN DATATYPE:")
a = True
print(a)	# display the value of a
print(type(a))  # display the data type of a

a = 2
b = 4
print(bool(a==b))	# Returns false as a is not equal to b
print(a==b)

a = None
print(bool(a))		# Returns False as a is None

a = ()
print(bool(a))		# Returns false as a is an empty sequence

a = 0.0
print(bool(a))		# Returns false as a is 0

a = 10
print(bool(a))		# Returns true as a is 10

print("\nNONE TYPE:")
x = None
print("x = ", x)
print("type of x = ", type(x))