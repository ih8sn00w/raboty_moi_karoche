"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №8 (6) (Выполнить транспонирование квадратной матрицы.)
"""

matrix = []

while True:
    # Запрашиваем ввод элемента строки
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения: ")

    # Проверяем, был ли введен элемент строки
    if row_input:
        # Разделяем введенные элементы и добавляем их в список
        row = list(map(int, row_input.split()))
        matrix.append(row)
    else:
        # Если введена пустая строка, завершаем ввод
        break

# Транспонирование матрицы

transposed_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transposed_matrix[j][i] = matrix[i][j]

# Вывод транспонированной матрицы

for row in transposed_matrix:
    print(row)
