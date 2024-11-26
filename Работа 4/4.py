def print_numbers(A, B):
    if A <= B:
          for num in range(A, B + 1):
              print(num)
else:
  for num in range(A, B - 1, -1):
    print(num)

# Пример использования
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print_numbers(A, B) 









               
