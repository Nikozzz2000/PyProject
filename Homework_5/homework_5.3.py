# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('homework_5.3.txt', 'r', encoding='utf-8') as my_f:
    value = []
    name = []
    my_f = my_f.read()
    line = my_f.split('\n')
    for i in line:
        i = i.split()
        if int(i[1]) <= 20000:
            name.append(i[0])
        value.append(i[1])

print(f'Оклад 20.000 и меньше у {name}\nсредний оклад {sum(map(int, value)) / len(value)}')
