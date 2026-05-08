def Hello(name,age=24):
    print(f"Your name is {name} and your age is {age}")


Hello(age=22,name="Ravi")  # keyword arguments
Hello(26,"Mohan") # positional arguments
Hello("Ravi")  # Default arguments
Hello ("Ravi",28) 