# syntax error, indentation error, tab error are some example of error which cannot be handled
# use case: 

"""
a = int(input("Enter any number"))
print(10/a)
print("i have done the division")

"""

# try, except, else, finally, raise

# try - wrap the block of code that might cause an exception
# except - handle the exception if it occurs
# else - run code only if no exception occurs
#finally - run code no matter what , whether there's an exception or not
# raise - manually throw an exception

a = int(input('Enter the value of a '))
try:
    print(10/a)
except Exception as err:
    print(f"Sorry there is an error as {err}")
else:
    print("Good there is no exception")
finally:
    print("i will run no matter what")
    
print("ok i have done the division")

