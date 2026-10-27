print("Введите координаты")

print("x:")
x = float(input())
while True:
    if x % 1 != 0:
        break
    if x % 1 == 0:
        print("Некорректный формат числа! Введите вещественное число.")
        print("x:")
        x = float(input())
    continue

print("y:")
y = float(input())
while True:
    if y % 1 != 0:
        break
    if y % 1 == 0:
        print("Некорректный формат числа! Введите вещественное число.")
        print("y:")
        y = float(input())
    continue

print(f"({x}, {y})")