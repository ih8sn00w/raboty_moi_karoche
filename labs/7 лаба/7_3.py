"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №7 #наибольшее кол-во пробелов
"""

count = int(input("Введите кол-во элементов в списке:"))
print("Введите числа по одному")
lst = [input() for i in range(count)]
print(lst)

ans = None
max_count = 0
for i, el in enumerate(lst):
    cur_count = 0
    for s in el:
        if s == " ":
            cur_count += 1
        else:
            if max_count < cur_count:
                max_count = cur_count
                ans = i
    if max_count < cur_count:
        max_count = cur_count
        ans = i

# Блок вывода
print(f"Строка, содержащая наибольшее количество пробелов ({max_count}) под индексом {ans}: {lst[ans]!r}")
