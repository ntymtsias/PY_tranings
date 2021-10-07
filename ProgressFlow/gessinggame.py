answer = 5
print ("Please guess number between 1 and 10: ")
guess = int(input())


if guess == answer:
    print("You got it.")
else:
    if guess < answer:
        print("Please, guess higher")
    else:
        print("Please, guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it")
    else:
        print("sorry you have not guessed correctly")
#
# if guess < answer:
#     print ("Please, guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
# elif guess > answer:
#     print ("Please, guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
# else:
#     print ("Congrats! U have guessed")
#
#
#




#
# x = 5
# y = 7
#
# if x == y:
#     print ("x equals y")
# elif x > y:
#     print ("x is greater than y")
# else:
#     print ("x is smaller than y")
#
# print()