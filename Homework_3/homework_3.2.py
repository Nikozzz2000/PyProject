# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_func(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


print(my_func(surname='Kot', name='Niko', year='1983', city='Munic', email='unknown@unknown.com', phone='0123456789'))
