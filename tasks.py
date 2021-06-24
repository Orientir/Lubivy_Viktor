# string = "Hello, "
# st = "world"
#
# new = string + st + "!"# конкатенация

st = "hello world!" # порядковый номер (индекс) - всегда начинается с нуля
s = "some string"
# print(st[1])   # []
# print(st[0:7]) # получить срез, правый крайний индекс не входит
# print(st[5:]) # получить срез, правый крайний индекс не входит, указываем шаг
# print(st[::-1]) # обратный индекс

# print(len(st)) # длина строки
# if_symbol = st.index("z") # ищет подстроку в строке
# if if_symbol == -1:
#     print("такого символа в строке нету")
# else:
#     print("Индекс элемента: ", if_symbol)

# new = st.replace("world", "friend")
# print(st)
# print(new)

# st = st.split(",")
# print(st)

# if st.istitle():
#     print("состоит из букв", st.istitle())
# else:
#     print("не состоит", st.istitle())

# st = st.upper()
# print(st)

# st = st.lower()
# print(st)

# sp = ["h", "e", "l", "l", "o"]
# print(sp)
# empty = ""
# x = "".join(sp)
# print(x)
# print(st.startswith("hello"))
# print(st.endswith("!"))

# symbol = ord("")
# symbol = chr(1010)
#
# print(symbol)



# # Задача 10
# # Вводится целое число, обозначающее код символа по таблице ASCII. Определить, это код английской буквы или какой-либо иной символ.

# symbol = int(input("Input code "))
#
# if (symbol >= 65 and symbol <= 90) or (symbol >= 97 and symbol <= 122):
#     print(symbol, " - ", chr(symbol), " it is english symbol")
# else:
#     print("it is some symbol: ", chr(symbol))

# % - нахождение остатка
# 4 / 2 = 2      4 % 2 = 0  - остатка нету, 4 делится нацело на 2
# 5 / 2 = 2.5    5 % 2 = 1 -    1 - это остаток
# 9 / 3 = 3      10 % 3 = 1    - 9 6 3
#                11 % 3 = 2    - 9 6 3  2