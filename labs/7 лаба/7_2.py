"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №7 #элементы кратные 3
"""

count = int(input("Введите кол-во элементов в списке:"))
print("Введите числа по одному")
lst = [int(input()) for i in range(count)]
up_lst = []
k = 0

for i in range(len(lst)):
    up_lst += [lst[i]]
    if lst[i] % 3 == 0:
        up_lst += [lst[i] * 2]

print(up_lst)
