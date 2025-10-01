#IMPLICIT CASTING
a=10   # int object
b=10.5 # float object
c=a+b
print("INTEGER PLUS FLOAT IS ",c)	#20.5

x=10
y=True
z=x+y
print ("BOOLEAN PLUS INTEGER IS ",z)

X=10.5
Y=True
Z=X+Y
print ("BOOLEAN PLUS FLOAT IS ",Z)

#EXPLICIT CASTING
print("\n TYPECASTING INT()")
a = int(10)		#(similar to a=10)
print("INT TO INT a is " ,a)			#10

a = int(10.5)		
print("FLOAT TO INT a is " ,a)			#10

a = int(2*3.14)		
print("FLOAT EXPRESSION TO INT a is " ,a)	#6

a=int(True)		
print("BOOLEAN TO INT a is " ,a)		#1

a = int("100")		
print("STRING TO INT a is " ,a)			#100

a = int("10"+"01")	
print("CONCATE STRING TO INT a is " ,a)		#1001

#a = int("10.5")	#ValueError: invalid literal for int() with base 10: '10.5'
#a = int("Hello World") #invalid literal for int() with base 10: 'Hello World'

#The int() function also returns integer from binary, octal and hexa-decimal string.
a = int("110011", 2)
print("BINARY TO INT a is " ,a)			# 51

a = int("20", 8)
print("OCTAL STRING TO INT a is " ,a)		#16

a = int("2A9", 16)
print("HEXA-DECIMAL STRING TO INT a is " ,a)	#681





