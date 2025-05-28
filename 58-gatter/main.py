import asyncio


async def fetch_data(data: int):
    print("Fetching data...")
    await asyncio.sleep(1)

    if data == 0:
        raise Exception("No Data...")

    return {"data": data}


async def main():
    # tasks = asyncio.gather(fetch_data(100), fetch_data(200), fetch_data(300))
    # tasks = asyncio.gather(
    #     fetch_data(100),
    #     fetch_data(200),
    #     fetch_data(300),
    #     fetch_data(0),
    # )  # Exception: No Data...
    tasks = asyncio.gather(
        fetch_data(100),
        fetch_data(200),
        fetch_data(300),
        fetch_data(0),
        return_exceptions=True,
    )
    results = await tasks
    print(results)


asyncio.run(main())
