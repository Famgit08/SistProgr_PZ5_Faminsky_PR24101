# import threading
# def print_numbers(start, finish):
#     for i in range(start, finish):
#         print(i)
# thread = threading.Thread(target=print_numbers, args=(1,10));
# thread.start()
# #thread.join()
# print_numbers(51,60)


import threading
import queue
import time
import random

#Очередь задач и результатов
task_queue = queue.Queue()
result_queue = queue.Queue()

def worker():
    """Поток-работник: берет задачу, выполняет, кладет результат"""
    while True:
        try:
            # Ждем задачу (неблокирующий режим с таймаутом)
            task = task_queue.get(timeout=1)
        except queue.Empty:
            break

        # Имитация работы
        time.sleep(random.uniform(0.1, 0.3))
        result = f"Обработано: {task}"
        result_queue.put(result)
        task_queue.task_done()

# Создаем 3 потока работника
threads = []
for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()
    threads.append(i)

# Добавляем 10 задач
for i in range(10):
    task_queue.put(f"Задача {i}")

# Завершение всех задач