# from multiprocessing import Process, Pipe



# def worker(connection):
#     question = connection.recv()
#     print("Получено: ", question)

#     connection.send("ответ готов")
 


# if __name__ == "__main__":
#     parent_conn, child_conn = Pipe()

#     process = Process(target=worker, args=(child_conn,))
#     process.start()


#     parent_conn.send("Выполнить задачу")
#     answer = parent_conn.recv()

#     print(answer)
#     process.join()

###################################################

# from multiprocessing import Process, Queue



# def worker(queue):
#     queue.put("Данные от дочернего процесса")


# if __name__ == "__main__":
#     queue = Queue()

#     process = Process(
#         target=worker,
#         args=(queue,)
#     )


#     process.start()


#     message = queue.get()
#     print(message)


#     process.join()


##########################################


from multiprocessing import Process, Queue

def producer(queue, start):
    for number in range(start, start + 3):
        queue.put(number)

if __name__ == "__main__":
    queue = Queue()

    processes = [
        Process(target=producer, args=(queue, 0)),
        Process(target=producer, args=(queue, 100))
    ]

for process in processes:
    process.start()

for process in processes:
    process.join()

while not queue.empty():
    print(queue.get())