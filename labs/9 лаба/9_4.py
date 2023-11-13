"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №9 (4)
"""

D = []
while True:
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения: ")
    if row_input:
        row = list(map(int, row_input.split()))
        D.append(row)
    else:
        break

II = list(map(int, input("Введите номера строк, для которых необходимо определить максимальный элемент. ").split()))

R = []

for i in II:
    max_element = max(D[i])
    R.append(max_element)

average = sum(R) / len(R)

print("\nМатрица D:")
for row in D:
    print(*row)
print("\nМассив I:")
print(*II)
print("\nМассив R:")
print(*R)
print("\nСреднее арифметическое значение:")
print(average)
