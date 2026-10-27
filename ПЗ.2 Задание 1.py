import random
import threading
import time
from concurrent.futures import ProcessPoolExecutor

results_threads = []
lock = threading.Lock()

def process_sublist_thread(sublist):
    total = sum(sublist)
    average = total / len(sublist)
    with lock:
        results_threads.append((total, average))

def process_sublist_process(sublist):
    total = sum(sublist)
    average = total / len(sublist)
    return (total, average)

if __name__ == "__main__":
    numbers = [random.randint(1, 1000) for _ in range(10000)]
    sublists = [numbers[i:i + 1000] for i in range(0, 10000, 1000)]

    start = time.time()
    threads = []
    for sublist in sublists:
        thread = threading.Thread(target=process_sublist_thread, args=(sublist,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    thread_time = time.time() - start

    print(f"Потоки: {thread_time:.4f} сек")

    start = time.time()
    with ProcessPoolExecutor() as executor:
        results_processes = list(executor.map(process_sublist_process, sublists))
    process_time = time.time() - start

    print(f"Процессы: {process_time:.4f} сек")

    print(f"\n=== СРАВНЕНИЕ ===")
    print(f"Потоки:   {thread_time:.4f} сек")
    print(f"Процессы: {process_time:.4f} сек")
    if thread_time < process_time:
        print("Потоки быстрее")
    else:
        print("Процессы быстрее")