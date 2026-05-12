age = int(input("Tell your age: "))


try:
    if age < 10 or age >18:
      raise ValueError("Sorry you cannot be registered")
    else:
      print("Welcome to the club.")
except Exception as err:
   print(f"an error occured as {err}")

print("The club will start soon..")