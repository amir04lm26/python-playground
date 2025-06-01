import threading
import time


def infinite_loop():
    while True:
        print(time.time())
        time.sleep(1)


# NOTE: Daemon thread
"""
    In Python, a daemon thread is a thread that runs in the background and does not block the
    main program from exiting. When all non-daemon threads (also called main or user threads)
    have finished execution, the program will exit even if daemon threads are still running.
"""

# NOTE: Key Characteristics of Daemon Threads:
"""
- Daemon threads are killed automatically when the main thread exits.
- They're typically used for background tasks that should not prevent
  the program from shutting down (e.g., logging, monitoring, housekeeping).
- Daemon threads are not joined automatically, and their cleanup is not guaranteed.
"""

if __name__ == "__main__":
    thread = threading.Thread(target=infinite_loop, daemon=True)  # Low priority threads

    thread.start()
