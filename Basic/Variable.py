#id()
print("id() output:")
month="May"
print(month)
print(id(month)) #id() fuction returns address of month variable
age=18
print(age)
print(id(age))
print("\n")	#new line

#create and print variable
#we cane write down this: print("\n create and print variable output:")	and delete print("\n")

print("create and print variable output:")		
counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Zara Ali"   # Creates a string variable
print (counter)	       # Print Variable
print (miles)
print (name)

#Delete variable
#del counter		#Delete variable
#print (counter)

#type() FUNCTION
print("\n type() output:")
x = "Zara"
y =  10
z =  10.10
print(type(x)) 		# get the data type of variable using the python built-in function type()
print(type(y))
print(type(z))
print("\n")

#Casting Python Variables
print("\n Casting Python Variables output:")
x = str(10)    # x will be '10'
y = int(10)    # y will be 10 
z = float(10)  # z will be 10.0
print( "x =", x )
print( "y =", y )
print( "z =", z )
print("\n")

#Case-Sensitivity of Python Variables
print("\n Case-Sensitivity of Python Variables output:")
age = 20
Age = 30
print( "age =", age )
print( "Age =", Age )	# Age and age are two different variables

#sinle assignment
print("\n Single Assignment")
a=10
b=10
c=10
print (a)
print (b)
print (c)

#multiple Assignment With Same Value
print("\n Multiple Assignment With Same Value output:")
a=b=c=10
print (a,b,c)

a = b = c = 100
print (a)
print (b)
print (c)

#multiple Assignment With Different Value
print("\n Multiple Assignment With Different Value output:")

a,b,c = 10,20,30
print (a,b,c)

a,b,c = 1,20.0,"Zara Ali"
print (a)
print (b)
print (c)

# Valid Naming Convention
print("\n valid Naming Convention output:")
counter = 100
_count  = 100
name1 = "Zara"
name2 = "Nuha"
Age  = 20
zara_salary = 100000
print (counter)
print (_count)
print (name1)
print (name2)
print (Age)
print (zara_salary)

# Invalid Naming Convention
'''
1counter = 100
$_count  = 100
zara-salary = 100000
print (1counter)
print ($count)
print (zara-salary)
'''

#Area & Parameter of rectangle
width = 10
height = 20
area = width*height
perimeter = 2*(width+height)
print ("\n Area = ", area)
print ("Perimeter = ", perimeter)

# Local Variable
print("\n Local Variable Output")
def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))	#print(x) we cannot use x or y outside the fuction

# Global Variable
print("Global Variable Output")
x = 5
y = 10
def sum():
   sum = x + y
   return sum
print(sum())
print(x) 		#we can use x or y outside the fuction
