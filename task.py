import time
from aiohttp import ClientSession
import asyncio

from asyncio.locks import Semaphore

URL = 'http://localhost:3009/long?a={}'

async def fetch_async(num):
    async with ClientSession() as session:
        async with session.get(URL.format(num)) as response:
            data = await response.json()
            return data['args']['a']

async def print_result(num,semaphore):
    async with semaphore:
        r = await fetch_async(num)
        print(f'fetch({num}) = {r}')

async def main(loop):
    now = time.time()
    semaphore = asyncio.Semaphore(3)
    tasks = [print_result(num,semaphore) for num in range(10)]
    await asyncio.wait(tasks)
    print('total use time:',time.time()-now)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()