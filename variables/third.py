#type Conversion

# int() float() str() bool()  these type conversion function

a = 12
print(type(a))

a = str(a)
print(type(a))

b = "1" # "one" value must be numerical
print(type(b))

b = int(b)
print(type(b))

 
# falsy values => False 0 0.0 " " [] {} () 

c = 10
c = bool(c)
print(type(c))


print(12/3)  # explicit conversion , int to float