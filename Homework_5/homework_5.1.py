# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_f = open('homework_5.1.txt', 'w')
line = input('Введите текст ')
while line:
    my_f.writelines([line, '\n'])
    line = input('Введите текст ')
    if not line:
        break

my_f.close()
my_f = open('homework_5.1.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

# как реализовать это задание с with open('text.txt', 'w') as my_f:
