from random import randint

def read_two_ints(prompt1="Введите количество строк: ", prompt2="Введите количество столбцов: "):
    s = input(prompt1).strip()
    parts = s.split()
    if len(parts) >= 2:
        return int(parts[0]), int(parts[1])
    rows = int(parts[0]) if parts else int(input(prompt1))
    cols = int(input(prompt2))
    return rows, cols

rows, cols = read_two_ints()

matrix = [[randint(-10, 10) for j in range(cols)] for i in range(rows)]

print("Матрица:")
for row in matrix:
    print(row)

new_matrix = list(
    map(
        lambda row: [row[0] ** 3] + row[1:],
        matrix
    )
)

print("Новая матрица:")
for row in new_matrix:
    print(row)