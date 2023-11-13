"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №7 #замена заглавных на строчные
"""


count = int(input("Введите кол-во элементов в списке:"))
print("Введите числа по одному")
lst = [input() for i in range(count)]
print(lst)

key = "QWERTYYUIOPASDFGHJKLZXCVBNM"


# Блок вычислений
for i in range(len(lst)):
    el = lst[i]
    should_change = False
    for j in range(len(el)):
        if el[j] in key:
            should_change = True
            el = el[:j] + el[j].lower() + el[j + 1:]
    if should_change:
        lst[i] = el

# Блок вывода
for i, el in enumerate(lst):
    print(f"lst[{i}]={el!r}")
