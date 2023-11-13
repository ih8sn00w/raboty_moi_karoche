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

ind = int(input("Введите индекс элемента, который хотите удалить: "))

lst_up = []
i = 0

while ind != i:
    lst_up.append(lst[i])
    i += 1
for q in range(i + 1, len(lst)):
    lst_up.append(lst[q])

print("Обновлённый список: ", lst_up)
