"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №6 (2b)
"""

value = float(input("Введите кол-во элементов в списке: "))

if value <= 0:
    print("Кол-во элементов слишком мало.")
    exit()
elif value != int(value):
    print("Кол-во элементов должно быть целым числом")
    exit()

lst = []
i = 0
for i in range(int(value)):
    a = float(input("Введите элемент в список: "))
    lst.append(int(a))

print(lst)

negative = 0
max_negativ = 10 ** 10

positive = 0
max_positve = 0

for i in range(1, len(lst)):
    if lst[i] < lst[i - 1]:
        if abs(lst[i]) % 2 == 1:
            negative = lst[i]
            max_negativ = min(negative, max_negativ)
    else:
        if abs(lst[i - 1]) % 2 == 1:
            negative = lst[i - 1]
            max_negativ = min(negative, max_negativ)

print(f"Минимальный нечётный элемент: {max_negativ}, его индекс: {lst.index(max_negativ)}")

for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        if abs(lst[i]) % 2 == 0:
            positive = lst[i]
            max_positve = max(positive, max_positve)
    else:
        if abs(lst[i - 1]) % 2 == 0:
            positive = lst[i - 1]
            max_positve = max(positive, max_positve)

print(f"Максимальный чётный элемент: {max_positve}, его индекс: {lst.index(max_positve)}")

a = max_positve
b = lst.index(max_positve)
c = max_negativ
d = lst.index(max_negativ)

lst.pop(d)
lst.insert(d, a)

lst.pop(b)
lst.insert(b, c)

print("Обновлённый список: ", lst)
