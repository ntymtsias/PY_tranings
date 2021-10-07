# parrot = "Norwegian Blue"
#
# letter = input("Enter character: ")
#
# if letter in parrot:
#     print("{} is in {}".format(letter,parrot))
#     print("letter was found at position of {}".format(parrot.find(letter)))
# else:
#     print ("I do not need that letter")
#
# print()

name = input("Please provide your name: ")
age = int(input("Please provide your age: "))
if name:
    if 18 <= age <= 30:
        print("Hi, {}\nYou are welcome to our party.".format(name.capitalize()))
    else:
        print("Hi, {}\nUnfortunately you are not matching the profile.".format(name.capitalize()))
else:
    print("You have provided empty name please try again")