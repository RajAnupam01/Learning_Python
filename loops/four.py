n = int(input("Please enter a random number "))

s=0
for i in range(0,n+1):
    s += i
print(f"The sum of number upto {n} is {s}")


f=1
for i in range(1,n+1):
    f *= i
print(f"The factorial of number upto {n} is {f}")
