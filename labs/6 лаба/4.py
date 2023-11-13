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

lenght = 1
max_lenght = 0

for i in range(1, len(lst)):
    if lst[i] > lst[i - 1] and lst[i] % 2 == 0 and lst[i - 1] % 2 == 0:
        lenght += 1
        max_lenght = max(lenght, max_lenght)
    else:
        lenght = 1
print(max_lenght)
