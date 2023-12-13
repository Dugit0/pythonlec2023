import asyncio
from collections import Counter

async def sender(queue, pattern):
    for el in pattern:
        await queue.put(el)
    await queue.put(None)

async def reader(queue, number):
    cnt = Counter()
    cur_number = 0
    while cur_number != number:
        key = await queue.get()
        if key is None:
            cur_number += 1
        else:
            cnt[key] += 1
    return cnt





