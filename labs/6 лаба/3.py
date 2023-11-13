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

ind = int(input("Введите номер экстремума: "))

q = 0
is_ext_found = False

for i in range(1, len(lst) - 1):
    if (lst[i] > lst[i + 1] and lst[i] > lst[i - 1]) or (lst[i] < lst[i + 1] and lst[i] < lst[i - 1]):
        q += 1
    if q == ind:
        print(f"Экстремум равен: {lst[i]}")
        is_ext_found = True
        break

if not is_ext_found:
    print("Экстремум не найден!")
