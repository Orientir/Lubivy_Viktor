# "Какой-то текст, какая-то информация, и т.д."
# bolean - True, False
# ["string", 2, True, [1, 2, 3], ]

# string = "some string"
# product = ["bread", "apples", "eggs", "cheese", "milk", "cherry"]
#
# print("**********************")
# print(string[0], " --string--")
# print(product[0], " --list--")
# print("**********************")
# print("\n")
#
# print("**********************")
# print(string[-1], " --string--")
# print(product[-1], " --list--")
# print("**********************")
# print("\n")
#
# print("**********************")
# print(string[5], " --string--")
# print(product[1], " --list--")
# print("**********************")
# print("\n")
#
# print("**********************")
# print(len(string), " --string--")
# print(len(product), " --list--")
# print("**********************")
# print("\n")
#
#
# new_list = product.copy()
# product.append("bananas")
# cherry = product.count("cherry") # count cherry in list
# print("**********************")
# print(string + " new", " --string--")
# print(product.count("cherry"), " --list--")
# print("**********************")
# print("\n")
#
# print("**********************")
# print(product.index("cherry"), " --list--")
# print("**********************")
# print("\n")
#
# product.insert(1, "water") # append on some index
# product.remove("water") # append on some index
# l = product.pop(2) # append on some index
#
# print("**********************")
# print(l, " --list--")
# print("**********************")
# print("\n")
#
# product.reverse()
#
# print("**********************")
# print(product, " --list--")
# print("**********************")
# print("\n")
#
# product.sort()
#
# print("**********************")
# print(product, " --list--")
# print("**********************")
# print("\n")

# if "2" in string:
#     print("Yes")
# else:
#     print("No")

# if "butter" in product:
#     print("Yes")
# else:
#     print("No")

# string = "some string"
# shop = ["bread", "eggs", "water", "milk", "cheese", "chokolate"]
# product = ["bread", "apples", "eggs", "milk", "water", "cherry"]
#
# for item in product:
#     print(item, " - item")
#     if item in shop:
#         print("in shop")
#         product.remove(item)
#     print("****")
# print(product)

# digit, Capslock, small letter, *, -, !, len 8 elements
passw_user = input("input password: ")  # "123Asd*!"

is_len = False
is_digit = False
is_upper = False
is_lower = False
is_special = False

if len(passw_user) != 8:
    print("Len of password must be equal 8 ")
else:
    is_len = True
    for item in passw_user:
        if item.isdigit():
            is_digit = True
        elif item.isupper():
            is_upper = True
        elif item.islower():
            is_lower = True
        elif item in ["*", "!", "-"]:
            is_special = True

