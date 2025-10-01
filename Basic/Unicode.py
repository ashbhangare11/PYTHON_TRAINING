var = "3/4"		#Unicode character
print (var)		#3/4

var = "\u00BE"		#Unicode value 
print (var)		#¾

var = "\u0031\u0030"	#string '10' is stored using the Unicode values of 1 and 0 which are \u0031 and u0030.
print (var)		#10

print("\nENCODE AND DECODE")
print("Hello Example")
string = "Hello"
tobytes = string.encode('utf-8')
print ("Encode(): string to byte: " ,tobytes)	# b'Hello'
string = tobytes.decode('utf-8')
print ("Decode(): Byte to string: " ,string)	# Hello

print("\n₹ Example")
string = "\u20B9"
print (string)					##₹
tobytes = string.encode('utf-8')
print ("Encode(): string to byte: " ,tobytes)	# b'\xe2\x82\xb9'
string = tobytes.decode('utf-8')
print ("Decode(): Byte to string: " ,string)	#₹