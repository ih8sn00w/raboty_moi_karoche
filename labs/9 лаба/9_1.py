"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №9 (1)
"""
import math

d = list(map(int, input("Введите чиcла через пробел в превый список: ").split()))
print(d)

f = list(map(int, input("Введите чиcла через пробел в превый список: ").split()))
print(f)

a = []

for j in range(len(d)):
    row = []
    for k in range(len(f)):
        row.append(round(math.sin(d[j] + f[k]), 3))
    a.append(row)

print(a)

AV = []
L = []

for row in a:
    pos_num = [num for num in row if num > 0]
    if pos_num:
        avg = sum(pos_num) / len(pos_num)
        AV.append(avg)
        L.append(sum(1 for num in row if num < avg))
    else:
        AV.append("-")
        L.append("-")

print("Матрица A: ")
for i in range(len(a)):
    print(f"{a[i]}, {AV[i]:.2g}, {L[i]}")
