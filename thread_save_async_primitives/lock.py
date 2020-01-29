import threading
import asyncio


class AsyncLock:
    """
    thread save async lock
    takes an async event loop and a lock.
    by default threading.lock is used.

    AsyncLock can be uses in an async with statement.
    the underlaying lock is exposed as lock attribute.
    """
    def __init__(self, loop: asyncio.AbstractEventLoop, lock: threading.Lock = None):
        self._loop: asyncio.AbstractEventLoop = loop
        self.lock = lock
        if self.lock is None:
            self.lock = threading.Lock()

    async def acquire(self, *args):
        return await self._loop.run_in_executor(None, self.lock.acquire, *args)

    async def release(self):
        return await self._loop.run_in_executor(None, self.lock.release)

    async def locked(self):
        return await self._loop.run_in_executor(None, self.lock.locked)

    async def __aenter__(self):
        await self.acquire()
        return self

    async def __aexit__(self, *_):
        await self.release()
