import asyncio

class FilterQueue(asyncio.Queue):
    def __init__(self, maxsize=0):
        return super().__init__(maxsize)

    @property
    def window(self):
        if self.empty():
            return None
        return self._queue[0]

    def __contains__(self, filter):
        for el in self._queue:
            if filter(el):
                return True
        return False

    def later(self):
        cur_el = self.get_nowait()
        return self.put_nowait(cur_el)

    async def get(self, filter=lambda a: False):
        if filter in self:
            while True:
                if filter(self.window):
                    return await super().get()
                else:
                    self.later()
        return await super().get()


