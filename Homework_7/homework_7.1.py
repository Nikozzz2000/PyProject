# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, n_1_1, n_1_2, n_1_3, n_2_1, n_2_2, n_2_3, n_3_1, n_3_2, n_3_3):
        self.line_1_1 = [n_1_1, n_1_2, n_1_3]
        self.line_1_2 = [n_2_1, n_2_2, n_2_3]
        self.line_1_3 = [n_3_1, n_3_2, n_3_3]

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.line_1_1)):
            number = self.line_1_1[i] + other.line_1_1[i]
            new_matrix.append(number)
            i += 1
        for i in range(len(self.line_1_2)):
            number = self.line_1_2[i] + other.line_1_2[i]
            new_matrix.append(number)
            i += 1
        for i in range(len(self.line_1_3)):
            number = self.line_1_3[i] + other.line_1_3[i]
            new_matrix.append(number)
            i += 1
        return new_matrix

    def __str__(self):
        return f'{str(self.line_1_1)}\n{str(self.line_1_2)}\n{str(self.line_1_3)}'


my_matrix_1 = Matrix(3, 5, 2, 4, 5, 9, 7, 4, 6)
my_matrix_2 = Matrix(2, 4, 5, 7, 4, 6, 4, 5, 9)
print(my_matrix_1 + my_matrix_2)
