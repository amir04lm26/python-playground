# GIL -> Global Interpreter Lock
"""
The GIL (Global Interpreter Lock) is a mutex (or lock) used in CPython,
the standard and most widely used implementation of Python. It allows
only one thread to execute Python bytecode at a time, even on multi-core processors.
"""

# 🔄 1. Async (asyncio) – Cooperative Concurrency - one block at a time
"""
Single-threaded, non-blocking, event-driven.
Tasks cooperate by yielding control (with await) back to the event loop.
Best for I/O-bound operations: web requests, database calls, file I/O, etc.
"""


# 🧵 2. Threading – Preemptive Concurrency - one line at a time
"""
Uses real OS threads (but subject to the GIL in CPython).
Best for I/O-bound tasks with blocking calls (e.g., file/network I/O).
Multiple threads can run "concurrently", but not truly in parallel for CPU-bound tasks due to the GIL.
"""


# 🧠 Key Differences
"""
Feature	        asyncio (Async/Await)	        threading
Model	        Cooperative	                    Preemptive
Threads Used	1	                            Multiple (OS-level)
GIL Impact	    Not affected (mostly)	        GIL limits CPU-bound parallelism
Best For	    I/O-bound, high concurrency	    I/O-bound, blocking code
Syntax	        async def, await	            Thread objects
CPU-bound Work	❌ Use multiprocessing instead	❌ Use multiprocessing instead
"""


# 🔧 When to Use What?
"""
Use Case	                                        Use This
High I/O concurrency (e.g., 1000 HTTP requests)	    asyncio
Blocking I/O with existing libraries	            threading
CPU-intensive processing	                        multiprocessing
GUI apps needing background tasks	                threading
"""

# NOTE: asyncio example
"""
import asyncio

async def download():
    await asyncio.sleep(2)
    print("Download complete")

async def main():
    await asyncio.gather(*(download() for _ in range(3)))

asyncio.run(main())
"""


# threading vs asyncio
"""
| Feature        | `threading`                       | `asyncio`                           |
| -------------- | --------------------------------- | ----------------------------------- |
| Suitable for   | Blocking I/O                      | Non-blocking I/O                    |
| CPU-bound work | ❌ (use `multiprocessing` instead)| ❌ (use `multiprocessing` instead)   |
| Integration    | Works with sync libraries         | Requires async-compatible libraries |
| Scaling        | OK for small # of threads         | Excellent for 1000s of I/O tasks    |
| Complexity     | Moderate (OS-level threads)       | Higher (event loop + `await`)       |
"""


import threading
from time import sleep


def process_data(name: str, count: int):
    print(f"Starting {name}...")

    for i in range(count):
        print(name, i + 1, sep=": ")
        sleep(1)


if __name__ == "__main__":
    # process_data("Thread-1", 5)
    # process_data("Thread-2", 10)
    thread1 = threading.Thread(
        target=process_data, kwargs={"name": "Thread-1", "count": 5}
    )
    thread2 = threading.Thread(target=process_data, args=("Thread-2", 10))

    thread1.start()
    sleep(3)
    thread2.start()

    thread1.join()  # wait for this line to finish before moving on
    thread2.join()
