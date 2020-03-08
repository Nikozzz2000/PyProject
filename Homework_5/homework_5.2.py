# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_f = open('homework_5.2.txt', 'r')
content = my_f.readlines()
print(f'Количество строк в файле - {len(content)}')
my_f = open('homework_5.2.txt', 'r')
content = my_f.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_f.close()
