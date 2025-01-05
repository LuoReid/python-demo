import requests
import time
import asyncio
from aiohttp import ClientSession

r = 100000
url = "http://localhost:8080/{}"
# url = "http://localhost:3009/{}"


def demo():
    t1 = time.time()
    for i in range(r):
        res = requests.get(url.format(i))
        delay = res.headers.get('delay')
        d = res.headers.get('date')
        print("{}:{} delay {}".format(d, res.url, delay))
    print('use time:', time.time()-t1)

# demo()


async def fetch(n):
    async with ClientSession() as session:
        async with session.get(url.format(n)) as response:
            # delay = response.headers.get('delay')
            # d = response.headers.get('date')
            # print("{}:{} delay {}".format(d, response.url, delay))
            res = await response.read()
            print(res)
            return res

async def bound_fetch(sem,n):
    async with sem:
        await fetch(n)

async def run(loop, r):
    tasks = []
    sem = asyncio.Semaphore(1000)
    for n in range(r):
        task = asyncio.ensure_future(bound_fetch(sem,n))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    print(res)


def demo2():
    t1 = time.time()
    loop = asyncio.get_event_loop()

    # loop.run_until_complete(fetch())
    future = asyncio.ensure_future(run(loop, r))
    loop.run_until_complete(future)
    print('use time:', time.time()-t1)


demo2()
