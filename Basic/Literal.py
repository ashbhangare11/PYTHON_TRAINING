print("INT LITERAL:")
x = 28							# normal INT literal
print ("28 in Decimal is", x, type(x))

x = 0O34						# Using octal notation
print ("0O34 in octal is", x, type(x))

x = 0X1c						# Using Hexadecimal notation
print ("0X1c in Hexadecimal is", x, type(x))

# Using normal floating point notation
print("\nFLOAT LITERAL:")
x = 1.23						# normal float literal
print ("1.23 in normal float literal is", x, type(x))	

x = 1.23E5						# Using Scientific notation WITH +VE POWER	
print ("1.23E5 in scientific notation is", x, type(x))
	
x = 1.23E-2						# Using Scientific notation WITH -VE POWER
print ("1.23E-2 in scientific notation is", x, type(x))	


#Using literal notation of complex number
print("\nCOMPLEX TYPE LITERAL:")
x = 2+3j
print ("2+3j complex literal is", x, type(x))
y = 2.5+4.6j
print ("2.5+4.6j complex literal is", y, type(y))

print("\nSTRING LITERAL:")
var1='hello'
print ("'hello' in single quotes is:", var1, type(var1))

var2="hello"
print ('"hello" in double quotes is:', var1, type(var1))

var3='''hello'''
print ("'''hello''' in triple quotes is:", var1, type(var1))

var4="""hello"""
print ('"""hello""" in triple quotes is:', var1, type(var1))

var5='Welcome to "Python Tutorial" from TutorialsPoint'
print (var5)

var6="Welcome to 'Python Tutorial' from TutorialsPoint"
print (var6)

print("\nLIST LITERAL:")
L1=[1,"Ravi",75.50, True]
print (L1, type(L1))

print("\nTUPLE LITERAL:")
T1=(1,"Ravi",75.50, True)
print (T1, type(T1))

T1=1,"Ravi",75.50, True		#WITHOUT PARANTHESIS(WITHOUT())
print (T1, type(T1))

print("\nDICTIONARY LITERAL:")
capitals={"USA":"New York", "France":"Paris", "Japan":"Tokyo",
"India":"New Delhi"}
numbers={1:"one", 2:"Two", 3:"three",4:"four"}
points={"p1":(10,10), "p2":(20,20)}

print (capitals, type(capitals))
print (numbers, type(numbers))
print (points, type(points))

