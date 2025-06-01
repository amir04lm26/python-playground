import threading
import time


lock = threading.Lock()


def counter(limit: int, name: str):
    for i in range(limit):
        time.sleep(0.5)
        print(name, i + 1, sep=": ")


def task1():
    lock.acquire()
    counter(5, "T-1")
    lock.release()


def task2():
    lock.acquire()
    counter(5, "T-2")
    lock.release()


def task3():
    counter(5, "T-3")


def main():
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    thread3 = threading.Thread(target=task3)

    thread1.start()
    thread2.start()
    thread3.start()


if __name__ == "__main__":
    main()
