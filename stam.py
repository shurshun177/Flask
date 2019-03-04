def val(d):
    for j in ('a', 'b'):
        if not d[j]:
            return False
    return True

import asyncio

async def myWorker():
    print('Hellow world')

async def main():
    print('My main')



try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*[myWorker() for i in range(5)]))
except KeyboardInterrupt:
    pass
finally:
    loop.close()