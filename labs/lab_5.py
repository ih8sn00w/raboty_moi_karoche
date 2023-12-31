"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №5 “Сумма бесконечного ряда”

Составить программу вычисления суммы ряда (по варианту) с точностью до члена
ряда accuracy
"""

# Блок ввода переменных

value = float(input("Введите значение аргумента: "))
accuracy = float(input("Введите значение точности: "))
max_iterations = float(input("Введите максимальное кол-во итераций: "))
step = float(input("Введите шаг печати: "))

# Блок проверки коректности данных

if step != abs(int(step)):
    exit("Значение шага должно быть натуральным.")
elif max_iterations != abs(int(max_iterations)):
    exit("Значение максимального кол-ва итераий должно быть натуральным.")

a = "№ Итерации"
b = "t"
c = "s"

# Построение таблицы

print("-" * 49)
print(f"|{a:^15}|{b:^15}|{c:^15}|")
print("-" * 49)
n = 0  # Итерации
x = value  # Значение по x
t = 1 / ((2 * n + 1) * (x ** (2 * n + 1)))  # Сумма N-ого члена ряда
s = 0  # Сумма всего ряда

# Ввод значений в таблицу
# Запись происходит до тех пор пока:
# 1. Количество итераций не превысит разрешенные
# 2. Когда t>=0.1

while abs(t) > accuracy:
    if n <= max_iterations:
        t = 1 / ((2 * n + 1) * (x ** (2 * n + 1)))
        s += t
        if n % step == 0:  # Вывод итераций с шагом
            print(f"|{int(n):^15}|{t:^15.5g}|{s:^15.5g}|")
        n += 1
    else:
        print("-" * 49)
        print("Достигнуто максимальное кол-во итераций")
        print(f"Сумма ряда: {s:.5g}. На это потребовалось {int(n) - 1} итераций.")
        exit()
print("-" * 49)
print(f"Сумма ряда: {s:.5g}. На это потребовалось {int(n) - 1} итераций.")
