class MyClass:
    def __init__(self):				#Defines the constructor method __init__, which is automatically called when a new instance is created. 						#self refers to the instance being created.
        self.__private_var = "I am Private"	#private variable

    def __private_method(self):			#private method
        return "This is a private method"	

    def show_private(self):
        return self.__private_var + " and " + self.__private_method()

obj = MyClass()
print(obj.show_private())    			# ✓ Access through method
# print(obj.__private_method())  		# ✗ AttributeError
print(obj._MyClass__private_method())  		# ✓ Access using name mangling