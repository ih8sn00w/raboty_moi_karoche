"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №9 (5)
"""

from string import ascii_uppercase

matrix = []
while True:
    # Запрашиваем ввод элемента строки
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения: ")

    # Проверяем, был ли введен элемент строки
    if row_input:
        # Разделяем введенные элементы и добавляем их в список
        row = row_input.split(' ')
        matrix.append(row)
    else:
        # Если введена пустая строка, завершаем ввод
        break

# Вывод исходной матрицы
print("Исходная матрица:")
for row in matrix:
    print(*row)
key = {
    'asd': 1,
    'dsa': 2
}

# Замена гласных на точки
dictionary = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] in dictionary:
            matrix[i][j] = '.'

# Вывод преобразованной матрицы
print("\nПреобразованная матрица:")
for row in matrix:
    print(*row)
