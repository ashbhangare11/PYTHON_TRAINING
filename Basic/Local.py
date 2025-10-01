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
print(x)
