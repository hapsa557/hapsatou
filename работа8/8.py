def calculate_rectangle_area(length, width):
    return length * width

# Ввод данных от пользователя
rectangles = []
for i in range(3):
    print(f"Введите длину и ширину {i + 1}-го прямоугольника:")
    length = float(input("Длина: "))
    width = float(input("Ширина: "))
    area = calculate_rectangle_area(length, width)
    rectangles.append(area)

# Вывод площадей
for i, area in enumerate(rectangles):
    print(f"Площадь {i + 1}-го прямоугольника: {area}")
