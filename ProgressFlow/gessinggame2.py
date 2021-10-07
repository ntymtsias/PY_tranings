import random
highest = 100
answer = random.randint(1,highest)
print(answer) #TODO: remove this line after testing
counter = 0
guess = 0
print("Please guess number between 1 and {}: ".format(highest))
while answer != guess:
    counter += 1
    print("Try Nr {}".format(counter))
    guess = int(input())
    if guess == 0 or counter == 3:
        break
    if guess < answer:
        print("Please, guess higher")
    elif guess > answer:
        print("Please, guess lower")
    else:
        print("You got it.")

# TODO: remove below code
#
# if guess == answer:
#     print("You got it.")
# else:
#     if guess < answer:
#         print("Please, guess higher")
#     else:
#         print("Please, guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("sorry you have not guessed correctly")
