# A race condition occurs when two threads access a shared variable at the same time.

import threading
import time

lock = threading.Lock()


def edit(operation: str, amount: int, repeat: int):
    global value

    for _ in range(repeat):
        with lock:  # * to fix the issue
            temp: int = value
            time.sleep(0)  # for context switching
            if operation == "add":
                temp += amount
            elif operation == "subtract":
                temp -= amount

            time.sleep(0)
            value = temp


if __name__ == "__main__":
    value: int = 0

    adder = threading.Thread(target=edit, args=("add", 1000, 1_000_000))
    subtractor = threading.Thread(target=edit, args=("subtract", 1000, 1_000_000))

    adder.start()
    subtractor.start()

    print("Waiting for threads to finish...")

    adder.join()
    subtractor.join()

    print(f"{value = }")  # * Output: value = 1000000000 or -999998000 or ...
