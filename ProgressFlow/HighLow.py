low = 1
high = 100

print ("Please think of number between {} and {}".format(low,high))
input( "Please Enter to start")

guess = 1
counter = 0
while low != high:
    counter += 1
    guess = low + (high - low)//2
    high_low = input("My guess is {}. Should I guess higher (h), lower(l), "
                     "or the answer is correct(c)?"
                     .format(guess).casefold())
    if high_low == "c":
        print("I've cracked the number in {} guesses".format(counter))
        break
    elif high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess + 1
    else:
        counter -= 1
        print("Please enter 'h','l' or 'c'")
else:
    print("You thought of the number {}".format(low))
    print("I have guessed the number in {}".format(counter))


