"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №8 (3) (Найти столбец, имеющий наибольшее количество простых чисел.)
"""
from math import floor

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

prime_in_column = []

# Перебираем столбцы матрицы.

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        p = 0
        for k in range(2, (floor(matrix[j][i] ** (1 / 2)) + 1)):
            if matrix[j][i] % k == 0:
                p = 1
                break
        if p == 0:
            count += 1
    prime_in_column.append(count)
    count = 0

# Находим индекс (номер) столбца с максимальным количеством простых чисел.

a = prime_in_column.index(max(prime_in_column))

print(f"В столбце №{a + 1} наибольшее количество простых чисел, их {max(prime_in_column)}")
