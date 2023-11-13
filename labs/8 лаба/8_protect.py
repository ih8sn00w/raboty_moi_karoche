"""
Кучмистый Антон Романович  ИУ7-11Б
Лабораторная работа №8 (Защита)
"""

matrix = []

while True:
    # Запрашиваем ввод элемента строки
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения: ")

    # Проверяем, был ли введен элемент строки
    if row_input:
        # Разделяем введенные элементы и добавляем их в список
        row = list(map(int, row_input.split()))
        matrix.append(row)
    else:
        # Если введена пустая строка, завершаем ввод
        break

print(f"Исходная матрица: {matrix}")

for j in range(len(matrix)):
    matrix[j].insert(0, matrix[j][-1])
    del matrix[j][-1]

print(f"После циклического перехода : {matrix}")

a = matrix.pop()
matrix = [a] + matrix

print(f"После переноса наверх: {matrix}")
