import asyncio


async def fetch_data(data: int) -> dict[str, int]:
    print("Fetching data...")
    await asyncio.sleep(2)  # a async function to wait
    return {"data": data}


async def counter():
    for i in range(10):
        await asyncio.sleep(0.5)
        print(i)


# aka coroutine - a function that can be suspended and resumed
async def main():
    # ...  # Equivalent to 'pass', but more semantically "not implemented"
    task1 = asyncio.create_task(
        fetch_data(1)
    )  # it will try to run it as soon as it can
    task2 = asyncio.create_task(counter())

    data: dict[str, int] = await task1  # future
    print(data)

    await task2


asyncio.run(main())

"""
asyncio -> Python event loop (runs in the main thread)
future -> coroutine that returns a value
"""


# NOTE: 🧵 Threads vs 🌀 Coroutines
"""
Feature	                Thread	                                Coroutine (async/await)
Concurrency model	    Preemptive multitasking	                Cooperative multitasking
Runs in new thread?	    ✅ Yes	                                ❌ No, runs in the main thread
Scheduling	            OS or interpreter thread scheduler	    Python event loop (asyncio)
Good for...	            CPU-bound tasks	                        I/O-bound tasks (e.g. network, disk)
Can be paused/resumed?	Not easily	                            ✅ Yes, via await
Overhead	            Higher (thread stack, context switch)	Low (no context switch overhead)
"""
