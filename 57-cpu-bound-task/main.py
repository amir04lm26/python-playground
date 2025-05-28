import asyncio


async def counter():
    for i in range(10**10):
        print(i)
        if i % 10_000 == 0:
            await asyncio.sleep(0)
    

async def main():
    task = asyncio.create_task(counter())

    # This will continue printing the numbers
    await asyncio.sleep(1)
    task.cancel()
    print("Task cancelled!")

    await task


asyncio.run(main())
