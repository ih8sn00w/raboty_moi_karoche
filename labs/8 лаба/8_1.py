"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №8 (1)
(2. Наибольшее количество подряд идущих одинаковых элементов.)
"""

matrix = []

print("Ввод матрицы")

# Каждая строчка матрицы вводится отдельно (учитывая, что каждая матрица прямоугольна)

while True:
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения: ")
    if row_input:
        row = list(map(int, row_input.split()))
        matrix.append(row)
    else:
        break

print(matrix)

k, k_max = 1, 0

# Проходим по каждой строке матрицы и ищем одинаковые подряд идущие элементы

for i in range(len(matrix)):
    for j in range(len(matrix[i]) - 1):
        if matrix[i][j] == matrix[i][j + 1]:
            k += 1
        else:
            k_max = max(k, k_max)
            k = 1
    k_max = max(k, k_max)
    k = 1

print(f"Наибольшее количество одинаковых подряд идущих элементов: {k_max}")  # Выводим результат
