def rvrs(qq):
    return qq[::-1]


def positive(a):
    if a >= 0:
        return True
    else:
        return False


matrix = []

while True:
    row_input = input("Введите строку элементов через пробел или нажмите Enter для завершения: ")
    if row_input:
        row = list(map(int, row_input.split()))
        matrix.append(row)
    else:
        break

rvrs_matrix = list(map(rvrs, matrix))

res = []
for row in rvrs_matrix:
    filt_row = filter(positive, row)
    res.append(filt_row)

a = list(map(lambda r: list(filter(positive, r)), rvrs_matrix))
print(a)

# Вывод результата
for row in res:
    print(*row)
