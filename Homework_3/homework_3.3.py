# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(x, y, z):
    i = [x, y, z]
    total = []
    max_1 = max(i)
    total.append(max_1)
    i.remove(max_1)
    max_2 = max(i)
    total.append(max_2)
    print(sum(total))


my_func(3, 2, 1)
