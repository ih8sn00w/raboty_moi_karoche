"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №9 (6)
"""

# Инициализация матриц A и B
A = []
B = []

while True:
    # Запрашиваем ввод элемента строки
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения матрицы А: ")

    # Проверяем, был ли введен элемент строки
    if row_input:
        # Разделяем введенные элементы и добавляем их в список
        row = list(map(int, row_input.split()))
        A.append(row)
    else:
        # Если введена пустая строка, завершаем ввод
        break

while True:
    # Запрашиваем ввод элемента строки
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения матрицы B: ")

    # Проверяем, был ли введен элемент строки
    if row_input:
        # Разделяем введенные элементы и добавляем их в список
        row = list(map(int, row_input.split()))
        B.append(row)
    else:
        # Если введена пустая строка, завершаем ввод
        break

# Формирование матрицы C
C = [[A[i][j]*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Суммирование элементов в столбцах матрицы C
num_rows = len(C)
num_cols = len(C[0])

V = [0] * num_cols

for j in range(num_cols):
    for i in range(num_rows):
        V[j] += C[i][j]

# Вывод матриц A, B, C и массива V
print("Матрица A:")
for row in A:
    print(*row)

print("\nМатрица B:")
for row in B:
    print(*row)

print("\nМатрица C:")
for row in C:
    print(*row)

print("\nМассив V:")
print(*V)
