from multiprocessing import Process, Queue, Event, Lock
import time
import random

log_lock = Lock()
messages = ["Hello!", "How are you?", "Meeting at 5pm", "Don't forget the report"]

def sender(stop_event, message_queue):
    while not stop_event.is_set():
        message_text = random.choice(messages)
        message = {
            "sender": "sender",
            "receiver": "receiver",
            "type": "message",
            "content": message_text
        }
        message_queue.put(message)
        
        with log_lock:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"[SENDER] Отправлено: {message_text}\n")
        
        time.sleep(random.uniform(0.5, 1.5))


def receiver(stop_event, message_queue):
    while not stop_event.is_set():
        if not message_queue.empty():
            message = message_queue.get()
            message_text = message["content"]
            
            with log_lock:
                with open("log.txt", "a", encoding="utf-8") as f:
                    f.write(f"[RECEIVER] Получено: {message_text}\n")
            
            time.sleep(random.uniform(0.5, 1.5))
        else:
            time.sleep(0.5)


def logger(stop_event, message_queue):
    while not stop_event.is_set():
        if not message_queue.empty():
            with log_lock:
                with open("log.txt", "a", encoding="utf-8") as f:
                    f.write("[LOGGER] Очередь содержит сообщения\n")
        time.sleep(1)


if __name__ == "__main__":
    stop_event = Event()
    message_queue = Queue()
    
    with open("log.txt", "w", encoding="utf-8") as f:
        f.write("=== НАЧАЛО РАБОТЫ ===\n")
    
    sender_process = Process(target=sender, args=(stop_event, message_queue))
    receiver_process = Process(target=receiver, args=(stop_event, message_queue))
    logger_process = Process(target=logger, args=(stop_event, message_queue))
    
    sender_process.start()
    receiver_process.start()
    logger_process.start()
    
    time.sleep(10)
    
    stop_event.set()
    
    sender_process.join()
    receiver_process.join()
    logger_process.join()
    
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write("=== РАБОТА ЗАВЕРШЕНА ===\n")
    
    print("Работа завершена. Проверьте файл log.txt")