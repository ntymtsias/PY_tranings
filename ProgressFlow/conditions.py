age = int(input("How old are you "))


# if 16 <= age <= 65:
if age in range(16,66):
    print("Have a good day at work")
elif age > 65 :
    print("have a good time with grandchildren")
else:
    print("Enjoy your free time")
print("-" * 80 )