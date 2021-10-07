name = input("Please enter your name ")
age = int(input("How old are you ,{0}?".format(name)))
print (age)

if age < 9:
    print ("No, please come back in {} years".format(18-age))
    print ("No, you are too young to make any decisions".format(18-age))
elif age == 900 :
    print ("Sorry, Yoda, you die in Return of Jedi")

elif age >= 18:
    print ("Yes, you are old enough to vote")
    print("Please put x in the box")

# for i in range(12,15):
#     print("No. {} squared is {} and cubed is {:4}".format(i,i**2,i**i))
# print("*"*80)
#
# print (i)
# if i >= 14 :
#     print ("it works")



