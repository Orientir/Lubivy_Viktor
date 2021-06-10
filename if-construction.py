# Типы данных - int, float, str

# Математические операторы сравнения
# <, >, <=, >=, !=, ==
# 4<5, 5<=5, 10>12, 3!=2, 6==6

int_number = 12 # int
float_number = 12.5 # float
str_data = "Some string"

name = input("Input your name from keyboard: ")
age = int(input("Input your age from keyboard: "))

if age > 18:
    print("Ты уже совершеннолетний")
elif age > 16:
    print("У тебя уже есть паспорт")
else:
    print("Ты еще ребенок")