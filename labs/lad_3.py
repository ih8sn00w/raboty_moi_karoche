"""
Кучмистый Антон Романович ИУ7-11Б
Лабораторная работа №3
"""

from math import *

# Блок ввода координат точек

x1, y1 = map(int, input("Введите координаты первой точки через пробел: ").split())
x2, y2 = map(int, input("Введите координаты второй точки через пробел: ").split())
x3, y3 = map(int, input("Введите координаты третьей точки через пробел: ").split())

# Вычисление сторон треугольника

a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

# Проверка на существование треугольника

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольника не существует")
    exit()

# Вывод длин сторон треугольника

print(f"Длины сторон треугольника: {a:.5g} , {b:.5g} , {c:.5g}")

# Нахождение высоты через площадь

p = (a + b + c) / 2
Area = sqrt(p * (p - a) * (p - b) * (p - c))
height = min((2 * Area) / a, (2 * Area) / b, (2 * Area) / c)

# Вывод высоты из наибольшего угла

print(f"Высота наибольшого угла равна: {height:.5g}")

# Нахождение углов через аркосинус

csa = (c * c + b * b - a * a) / (2 * c * b)
csb = (a * a + c * c - b * b) / (2 * a * c)

ang1 = (acos(csa) * 180) // pi
ang2 = (acos(csb) * 180) // pi
ang3 = 180 - (ang1 + ang2)

# Определение вида треугольника

if max(ang1, ang2, ang3) > 90:
    print("Треугольник тупоугольный")
else:
    print("Треугольник не тупоугольный")

# Ввод координат точки

X, Y = map(int, input("Введите координаты точки через пробел: ").split())

# Проверка на нахождение точки в треугольнике

if ((x1 - X) * (y2 - y1) - (x2 - x1) * (y1 - Y)
    <= 0 and (x2 - X) * (y3 - y2) - (x3 - x2) * (y2 - Y)
    <= 0 and (x3 - X) * (y1 - y3) - (x1 - x3) * (y3 - Y)
    <= 0) or ((x1 - X) * (y2 - y1) - (x2 - x1) * (y1 - Y)
              >= 0 and (x2 - X) * (y3 - y2) - (x3 - x2) * (y2 - Y)
              >= 0 and (x3 - X) * (y1 - y3) - (x1 - x3) * (y3 - Y) >= 0):
    print("Точка находится внутри треугольника")  # строка вывода
    ad = abs((y2 - y1) * X + (x1 - x2) * Y + y1 * x2 - x1 * y2) / sqrt((y2 - y1) ** 2 + (x1 - x2) ** 2)
    bd = abs((y3 - y2) * X + (x2 - x3) * Y + y2 * x3 - x2 * y3) / sqrt((y3 - y2) ** 2 + (x2 - x3) ** 2)
    cd = abs((y3 - y1) * X + (x1 - x3) * Y + y1 * x3 - x1 * y3) / sqrt((y3 - y1) ** 2 + (x1 - x3) ** 2)
    if ad == 0 or bd == 0 or cd == 0:
        print("Точка на стороне треугольника")  # строка вывода
    else:
        print(f"Расстояние от точки до ближайшей стороны треугольника: {min(ad, bd, cd):.5g}")  # строка вывода
else:
    print("Точка не находится внутри треугольника")  # строка вывода

# Ввод второй точки

XX, YY = map(int, input("Введите кординаты второй точки через пробел: ").split())

# Алгоритм определения пересечения отрезка и треугольника

condition1 = (X - x1) * (YY - y1) - (Y - y3) * (XX - x1)
condition2 = (X - XX) * (y2 - YY) - (Y - YY) * (x2 - XX)
condition3 = (X - x3) * (Y - y3) - (Y - y3) * (x3 - X)

if (condition1 > 0) and (condition2 > 0) and (condition3 > 0):
    print("Отрезок проходит через треугольник")  # строка вывода
else:
    print("Отрезок не проходит через треугольник ")  # строка вывода
