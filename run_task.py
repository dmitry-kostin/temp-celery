import asyncio
from app.tasks import add


async def adding(a, b):
    job = add.apply_async((a, b))

    while True:
        await asyncio.sleep(0.5)
        if job.ready():
            if job.successful():
                return job.result


async def send_tasks(numbers):
    tasks = []
    for a, b in numbers:
        tasks.append(asyncio.ensure_future(adding(a, b)))
    return await asyncio.gather(*tasks)


async def main():
    numbers = ((1, 2), (3, 4), (10, 20),
               (1, 2), (3, 4), (10, 20))
    results = await send_tasks(numbers)
    print(results)
    return results


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
