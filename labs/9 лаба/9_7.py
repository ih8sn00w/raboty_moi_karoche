"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №9 (7)
"""

from math import inf

k = int(input("Введите кол-во матриц: "))
n = int(input("Введите кол-во строк матрицы: "))
m = int(input("Введите кол-во столбцов матрицы: "))

a = []

for z in range(k):
    a.append([])
    for i in range(n):
        a[z].append([])
        for j in range(m):
            a[z][i].append(float(input(f"Введите {j+1}-й элемент {i+1}-й строки {z+1}-й матрицы: ")))

minimum = -inf

for z in range(k):
    for i in range(n):
        for j in range(m):
            if len(str(a[z][i][j])) > minimum:
                minimum = len(str(a[z][i][j]))

s = int(input("Введите номер среза по второму индексу: "))

while s <= 0 or s >= m+1:
    print('Введено некорректное значение ')
    s = int(input("Введите номер среза по второму индексу: "))

print("Полученная матрица: ")
for j in range(n):  # Вывод соответствующего элемента: 1-й элемент j-й строки i-й матрицы
    for i in range(k):
        if i != k - 1:
            print(f'{a[i][j][s - 1]:^{minimum}}', end=' ')
        else:
            print(f'{a[i][j][s - 1]:^{minimum}}', end='\n')
