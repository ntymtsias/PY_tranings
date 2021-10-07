shopping_list = ["milk","jogurt","eggs","ham","rice","bread"]

# for items in shopping_list:
#     if items != "ham":
#         print ("Buy " + items)

for item in shopping_list:
    if item == "ham":
        break

    print("Buy " + item)