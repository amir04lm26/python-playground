import asyncio


async def fetch_data(data: int) -> dict[str, int]:
    print("Fetching data...")
    await asyncio.sleep(2)
    return {"data": data}


# # async def main():
# #     task = asyncio.create_task(fetch_data(100))  # feature
# #     await asyncio.sleep(0)
# #     print("Doing something...")
# #     data = await task
# #     print(data)


# Output:
"""
# added to the queue 
Doing something...
Fetching data...
{'data': 100}

# adding await asyncio.sleep(0)
Fetching data...
Doing something...
{'data': 100}
"""


# async def main():
#     task = asyncio.create_task(fetch_data(100))  # feature
#     await asyncio.sleep(1)
#     task.cancel()

#     # To access the result before/after it's done
#     # print(task.result())  # asyncio.exceptions.InvalidStateError: Result is not set.

#     print(task.cancelled())  # False

#     await asyncio.sleep(0)
#     print(task.cancelled())  # True

#     try:
#         data = await task
#         print(data)
#     except asyncio.CancelledError:
#         print("Task was cancelled...")


# async def main():
#     task = asyncio.create_task(fetch_data(100))  # feature
#     await asyncio.sleep(3)

#     if task.done():
#         data = task.result()
#         print(data)
#     else:
#         print("Data not ready!")


async def main():
    task = asyncio.create_task(fetch_data(100))  # feature
    # await asyncio.wait_for(task, 2) # TimeoutError

    try:
        data = await asyncio.wait_for(task, 3)
        print(data)
    except asyncio.TimeoutError:
        print("Timeout reached!")


asyncio.run(main())
