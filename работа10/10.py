matrix = []
with open('Худобина_У234_vvod.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matrix.append(row)
def swap_min_max(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    min_element = min([min(row) for row in matrix])
    max_element = max([max(row) for row in matrix])

    # индексы строки и столбца для наименьшего
    min_row = 0
    min_col = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == min_element:
                min_row = i
                min_col = j

    #  индексы строки и столбца для наибольшего
    max_row = 0
    max_col = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == max_element:
                max_row = i
                max_col = j

    # Меняем местами значения
    matrix[min_row][min_col], matrix[max_row][max_col] = matrix[max_row][max_col], matrix[min_row][min_col]

    return matrix
print("Исходная матрица:")
for row in matrix:
    print(row)
# Меняем местами
result_matrix = swap_min_max(matrix)
result_matrix_str = ' '.join(map(str, result_matrix))
print("Матрица после замены:")
for row in result_matrix:
    print(row)
with open('Худобина_У-234_vivod.txt', 'w') as file:
    file.write(result_matrix_str)
