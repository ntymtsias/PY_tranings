
opions_to_print = ["Learn", "Read", "Swimming", "dinner", "Go to bed", "Exit"]
counter = 0
choise = 10

while choise != 0:
    if choise in range(6):
        print("You chose {}".format(choise))
        # print(opions_to_print[choise - 1])
    else:
        print("Please choose your option from the list below: ")
        for options in opions_to_print:
            if options == "Exit":
                counter = 0
            else:
                counter += 1
            print("{}:\t{}".format(counter, options))
        # print("Please select valid option from 0 to 5")
    choise = int(input())
