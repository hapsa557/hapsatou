def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])

    # Проверка сумм строк
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    # Проверка сумм столбцов
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False

    # Проверка главной диагонали
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False

    # Проверка побочной диагонали
    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False

    return True

# Пример использования
matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

print(is_magic_square(matrix))  # Вывод: True
