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

n = len(matrix)

maxlen = 0

for i in range(n):
    for j in range(n):
        maxlen = max(maxlen, len(str(matrix[i][j])))

# Смена матрицы относительно главной диагонали
print("Изначальная матрица: ")
for x in matrix:
    print(*x)
num = 0
for i in range(n):
    for j in range(i + 1, n):
        down = matrix[j][i]
        right = matrix[i][j]
        matrix[i][j] = down
        matrix[j][i] = right
print("Транспонированная матрица:")
# Вывод матрицы
for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]: >{maxlen}}", end=" ")
    print()
