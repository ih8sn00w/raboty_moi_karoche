"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №9 (2)
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

N = len(matrix)

print("Исходная матрица")

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end='  ')
    print()

matrix_start = matrix

# разворот матрицы по часовой стрелке

for i in range(0, N, 2):
    for j in range(i, N - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[N - 1 - j][i]
        matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
        matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
        matrix[j][N - 1 - i] = temp

print("Матрица после поворота на 90 по часововой: ")

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end='  ')
    print()

print("Матрица после поворота на 90 против часововой: ")

# Разворот матрицы обратно против часовой стрелке

for i in range(0, N, 2):
    for j in range(i, N - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][N - 1 - i]
        matrix[j][N - 1 - i] = matrix[N - 1 - i][N - 1 - j]
        matrix[N - 1 - i][N - 1 - j] = matrix[N - 1 - j][i]
        matrix[N - 1 - j][i] = temp

# Вывод матрицы после обратного разворота
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end='  ')
    print()
