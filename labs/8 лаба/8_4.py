"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №8 (4) (Переставить местами столбцы с максимальной и минимальной суммой)
элементов.
"""

matrix = []

line = 0

# Ввод элементов матрицы от пользователя.

while True:
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения: ")
    if row_input:
        row = list(map(int, row_input.split()))
        matrix.append(row)
        line += 1
    else:
        break
print(matrix)

count = 0
sum_in_columns = []

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        count += matrix[j][i]
    sum_in_columns.append(count)
    count = 0

# Находим индексы столбцов с минимальной и максимальной суммой элементов.

index_column_min = sum_in_columns.index(min(sum_in_columns))
index_column_max = sum_in_columns.index(max(sum_in_columns))

# Переставляем значения между минимальным и максимальным столбцом в каждой строке матрицы.

for q in range(len(matrix)):
    matrix[q][max(index_column_min, index_column_max)], matrix[q][min(index_column_min, index_column_max)] = matrix[q][
        min(index_column_min, index_column_max)], matrix[q][max(index_column_min, index_column_max)]

print(f"Обновлённая матрица: {matrix}")
