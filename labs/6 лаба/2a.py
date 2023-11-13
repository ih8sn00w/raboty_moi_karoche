"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №6 (2a)
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

lst.pop(ind)

print("Обновлённый список: ", lst)
