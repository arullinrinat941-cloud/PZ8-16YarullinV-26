from random import randint

matrix = [[randint(-10, 10) for j in range(3)] for i in range(3)]

print("Матрица:")
for row in matrix:
    print(row)

positive = list(filter(lambda x: x > 0, sum(matrix, [])))

print("Среднее:", sum(positive) / len(positive))