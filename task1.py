import requests
import asyncio
from aiohttp import ClientSession
import time

URL = 'http://localhost:3009/long?num={}'
def hello(n):
    res = requests.get(URL.format(n))
    # print(res.text)
    return res.text

# hello()
#multi task:
def demo():
    t1 = time.time()
    for n in range(10):
        res = hello(n)
        print(res)
    print('use time:',time.time()-t1)

# demo()


async def fetch(n):
    async with ClientSession() as session:
        async with session.get(URL.format(n)) as response:
            res = await response.read()
            # print(res)
            return res

async def run(loop,r):
    tasks = []
    for n in range(r):
        task = asyncio.ensure_future(fetch(n))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    print(res)

def demo2():
    t1 = time.time()
    loop = asyncio.get_event_loop()
    
    # loop.run_until_complete(fetch())
    future = asyncio.ensure_future(run(loop,10))
    loop.run_until_complete(future)
    print('use time:',time.time()-t1)

demo2()

