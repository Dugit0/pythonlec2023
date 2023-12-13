import asyncio
from collections import Counter
async def serial(number, barrier):
    if not hasattr(barrier, 'my_flag'):
        barrier.my_flag = 0
        barrier.nums = []
        barrier.barrs = []
    barrier.nums.append(number)
    await barrier.wait()
    if barrier.my_flag == 0:
        barrier.nums.sort()
        cnt = Counter(barrier.nums)
        sort_set_num = sorted(list(set(barrier.nums)))
        barrier.barrs = [asyncio.Barrier(cnt[sort_set_num[0]])] + \
            [asyncio.Barrier(cnt[sort_set_num[i - 1]] + cnt[sort_set_num[i]]) for i in range(1, len(sort_set_num))]
        barrier.my_index = {key: val for val, key in enumerate(sort_set_num)}
        barrier.my_flag += 1
    cur_bar_ind = barrier.my_index[number]
    await barrier.barrs[cur_bar_ind].wait()
    print(number)
    if cur_bar_ind + 1 < len(barrier.barrs):
        await barrier.barrs[cur_bar_ind + 1].wait()


