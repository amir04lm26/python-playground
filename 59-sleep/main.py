import asyncio


async def main():
    print("Started!")
    # useful for mocking data
    data = await asyncio.sleep(1, result={"item": 123})
    print(data)


asyncio.run(main())
