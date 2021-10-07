number = input("Please input any separators with numbers ") #"9,223;373:036 854,775;807"
separators = ""
TotalSum = 0

for char in number:
    if not char.isnumeric():
        separators = separators + char
    else:
        TotalSum = TotalSum + int(char)

# print(separators)

print (TotalSum)

values = "".join(char if char not in separators else " " for char in number).split()

Sum = 0

for x in values:
    Sum = Sum + int(x)
print (Sum)


print ("Total sum = {}".format(sum([int(val) for val in values])))

print ("Total sum cubed = {}".format(sum([int(val)**int(val) for val in values])))
print ("Combunation = {}".format([int(val)**int(val) for val in values]))
