# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


# Целое число
a = 6

# Дробное число
b = 2.6

# Строка
c = "строка"

# Булевый
d = True

# Список
e = [1, 2, 3]

# Кортеж
f = (1, 2, 3)

# Множество
g = {"numeral": 1, "letter": "a"}

p = [a, b, c, d, e, f, g]
for i in p:
    print(type(i))
