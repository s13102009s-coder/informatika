import os
import time
import multiprocessing


def process_1():
    print("Функция 1: запуск процесса")
    time.sleep(2)
    print("Функция 1: процесс завершён")


def process_2():
    print("Функция 2: запуск процесса")
    time.sleep(3)
    print("Функция 2: процесс завершён")


def process_3():
    print("Функция 3: запуск процесса")
    time.sleep(1)
    print("Функция 3: процесс завершён")


def process_4():
    print("Функция 4: запуск процесса")
    time.sleep(4)
    print("Функция 4: процесс завершён")


if __name__ == "__main__":
    # Создаём четыре процесса
    p1 = multiprocessing.Process(target=process_1)
    p2 = multiprocessing.Process(target=process_2)
    p3 = multiprocessing.Process(target=process_3)
    p4 = multiprocessing.Process(target=process_4)

    # Запускаем процессы
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Выводим ID каждого процесса
    print(f"ID процесса 1: {p1.pid}")
    print(f"ID процесса 2: {p2.pid}")
    print(f"ID процесса 3: {p3.pid}")
    print(f"ID процесса 4: {p4.pid}")

    # Ожидаем завершения всех процессов
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    # Выводим результаты работы
    print("Результат работы функции 1: процесс завершён")
    print("Результат работы функции 2: процесс завершён")
    print("Результат работы функции 3: процесс завершён")
    print("Результат работы функции 4: процесс завершён")
    print("Все процессы завершены.")
