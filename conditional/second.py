t = int(input("Please tell the temperature "))

if t < 0:
    print("Freezing temp")
elif t >= 0 and t < 10:
    print("Very cold")
elif t >=20 and t < 30:
    print("Cold")
elif t >=30 and t < 40:
    print("Warm")
else:
    print('Hot')