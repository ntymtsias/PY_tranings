shopping_list = ["milk","jogurt","eggs","ham","rice","bread"]

item_to_find = "gg"
found_at = None

# Variant with break function
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

# Proper way of coding


if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

print (found_at)
# print (shopping_list[found_at])