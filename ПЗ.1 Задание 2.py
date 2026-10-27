with open("source.txt", "w", encoding="utf-8") as f:
    f.write("Первая строка\n")
    f.write("Вторая строка\n")
    f.write("Третья строка\n")

print("Создан исходный файл")

with open("source.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("target.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("Копирование завершено!")