"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №7 #удалить чётные элементы
"""

count = int(input("Введите кол-во элементов в списке:"))
print("Введите числа по одному")
lst = [int(input()) for i in range(count)]

new_index = 0

for i in range(len(lst)):
    if lst[i] % 2 != 0:
        lst[new_index] = lst[i]
        new_index += 1

lst[:] = lst[:new_index]

print(lst)
