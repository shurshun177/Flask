import requests
import time
import asyncio
from aiohttp import ClientSession
url = 'http://localhost:5000/'
async  def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()

async  def bound_fetch(sem, url, session):
    async with sem:
        await fetch(url, session)

async  def run(r):
    url = 'http://localhost:5000/'
    tasks = []
    sem = asyncio.Semaphore(1000)
    async  with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(bound_fetch(sem, url, session))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses

number = 10000
start = time.time()
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(number))
loop.run_until_complete(future)
elapsed_time = time.time() - start
print(elapsed_time, type(elapsed_time))
