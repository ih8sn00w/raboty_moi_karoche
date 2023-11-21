"""
Кучмистый Антон Романович ИУ7-11Б
Лабораторная работа №10
Вычисление приближённого значения интеграла
"""


def f(digit):
    return 2 * digit


def F(digit):
    return digit ** 2 + 10


start_pose = float(input('Введите начало отрезка: '))
end_pose = float(input('Введите конец отрезка: '))
count_1 = int(input('Введите колличество участков разбиения 1: '))
count_2 = int(input('Введите колличество участков разбиения 2: '))

# 1 способ 1 колличество разбиений

l1 = 0
for i in range(count_1):
    x = f(start_pose + ((end_pose - start_pose) / count_1) * i)
    dx = ((end_pose - start_pose) / count_1)
    l1 += x * dx
print(l1)

# 1 способ 2 колличество разбиений

l2 = 0
for i in range(count_2):
    a = f(start_pose + ((end_pose - start_pose) / count_2) * i)
    l2 += a * ((end_pose - start_pose) / count_2)
print(l2)

# 2 способ 1 колличество разбиений

l3 = 0
x2 = start_pose
for i in range(1, count_1 + 1):
    x1 = x2
    x2 = start_pose + ((end_pose - start_pose) / count_1) * i
    dx = ((end_pose - start_pose) / count_1)
    l3 += dx * (f(x1) + 3 * f((2 * x1 + x2) / 3) + 3 * f((x1 + 2 * x2) / 3) + f(x2)) / 8
print(l3)

# 2 способ 2 колличество разбиений

l4 = 0
x2 = start_pose
for i in range(1, count_2 + 1):
    x1 = x2
    x2 = start_pose + ((end_pose - start_pose) / count_2) * i
    dx = ((end_pose - start_pose) / count_2)
    l4 += dx * (f(x1) + 3 * f((2 * x1 + x2) / 3) + 3 * f((x1 + 2 * x2) / 3) + f(x2)) / 8
print(l4)

# Вывод таблицы

print('-' * 69)
print('|' + '-' * 28, '|' + f'{count_1:^18.7g}' + '|' + f'{count_2:^18.7g}' + '|')
print('-' * 69)
print('|' + ' метод левых прямоугольников ' + '|' + f'{l1:^18.7g}' + '|' + f'{l2:^18.7g}' + '|')
print('-' * 69)
print('|' + '          метод 3/8          ' + '|' + f'{l3:^18.7g}' + '|' + f'{l4:^18.7g}' + '|')
print('-' * 69)

# вычисление погршностей измерений
print("\n\n")

print("-" * 85)

print(f"|{'l1':^20}|{'l2':^20}|{'l3':^20}|{'l4':^20}|")

print("-" * 85)

a = F(start_pose)
b = F(end_pose)
q = b - a
dl1 = l1 - q
dl2 = l2 - q
dl3 = l3 - q
dl4 = l4 - q

print(f'|{dl1:^20.5g}|{dl2:^20.5g}|{dl3:^20.5g}|{dl4:^20.5g}|')
print("-" * 85)

dl1 = abs(dl1 / q * 100)
dl2 = abs(dl2 / q * 100)
dl3 = abs(dl3 / q * 100)
dl4 = abs(dl4 / q * 100)

print(f'|{dl1:^20.5g}|{dl2:^20.5g}|{dl3:^20.5g}|{dl4:^20.5g}|')
print("-" * 85)

# повышение точности

eps = 1e-4
if dl1 >= dl3 or dl2 > dl4:
    N = count_1
    while True:
        l = 0
        N = 2 * N
        for i in range(2 * N):
            x = f(start_pose + ((end_pose - start_pose) / N) * i)
            dx = ((end_pose - start_pose) / N)
            l += x * dx
        if abs(l1 - l) < eps:
            print(l, N)
            break
        l1 = l
else:
    N = count_2
    while True:
        l = 0
        N = 2 * N
        for i in range(2 * N):
            x = f(start_pose + ((end_pose - start_pose) / N) * i)
            dx = ((end_pose - start_pose) / N)
            l += x * dx
        if abs(l3 - l) < eps:
            print(l, N)
            break
        l3 = l
