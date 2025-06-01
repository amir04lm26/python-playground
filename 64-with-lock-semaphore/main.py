import threading
import time


sem = threading.Semaphore(5)


def process_something(id: int):
    with sem:  # works with locks as well
        print(f"{id} -> Running!")
        time.sleep(5)
        print(f"{id} -> Finished!")


if __name__ == "__main__":
    for i in range(10):
        time.sleep(0.5)
        thread = threading.Thread(target=process_something, kwargs={"id": i + 1})
        thread.start()
