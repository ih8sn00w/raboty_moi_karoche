"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №8 (2) (Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.)
"""

matrix = []

# Ввод элементов матрицы от пользователя.

while True:
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения: ")
    if row_input:
        row = list(map(int, row_input.split()))
        matrix.append(row)
    else:
        break
print("Получившаяся матрица:")
print(matrix)

neg = 0
lst = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            neg += 1
    lst.append(neg)
    neg = 0

# Находим индексы строки с минимальным и максимальным количеством отрицательных чисел.

mal = lst.index(min(lst))
bol = lst.index(max(lst))

a = matrix[bol]
b = matrix[mal]

matrix.insert(mal, a)
matrix.pop(mal + 1)
matrix.insert(bol, b)
matrix.pop(bol + 1)

print("Преобразованная матрица:")
print(matrix)
