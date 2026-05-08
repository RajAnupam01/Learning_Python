fruits = ['apple','mango','litchi','berry','melon']
digits = [11,22,33,44,55]
mixed_list = [12,31,True,"apple",print("hello")]

print(fruits[0])
print(digits[-1])
print(fruits[0:2:1])

for i in range(len(fruits)):
    print(fruits[i])

for i in fruits:
    print(i)


print(dir(list))