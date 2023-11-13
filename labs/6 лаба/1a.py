"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №6 (1а)
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

elem, ind = map(int, input("Введите значение и индекс для нового элемента: ").split())

lst.insert(ind, elem)

print("Обновлённый список: ", lst)
