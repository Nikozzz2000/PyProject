# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

# решить генерацию случайных чисел в my_list

import random

my_list = []
for i in range(10):
    a = random.randint(0, 99)
    my_list.append(a)

my_new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el - 1] < my_list[el]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
