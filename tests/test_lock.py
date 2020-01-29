from pathlib import Path
import sys
import asyncio
import pytest

sys.path.append(str(Path(__file__).parents[1]))
from thread_save_async_primitives import AsyncLock


def test_async_lock_starts_unlocked():
    loop = asyncio.new_event_loop()
    lock = AsyncLock(loop)
    assert loop.run_until_complete(lock.locked()) is False


def test_async_lock_is_locked_after_acquiring_the_lock():
    loop = asyncio.new_event_loop()
    lock = AsyncLock(loop)
    assert loop.run_until_complete(lock.acquire()) is True
    assert loop.run_until_complete(lock.locked()) is True


def test_async_lock_is_unlocked_after_releasing_the_lock():
    loop = asyncio.new_event_loop()
    lock = AsyncLock(loop)
    loop.run_until_complete(lock.acquire())
    loop.run_until_complete(lock.release())
    assert loop.run_until_complete(lock.locked()) is False


def test_async_lock_times_out_if_already_acquired():
    loop = asyncio.new_event_loop()
    lock = AsyncLock(loop)
    loop.run_until_complete(lock.acquire())
    assert loop.run_until_complete(lock.acquire(False)) is False


def test_async_lock_aquire_returns_if_the_lock_is_aquired():
    loop = asyncio.new_event_loop()
    lock = AsyncLock(loop)
    assert loop.run_until_complete(lock.acquire()) is True


def test_async_lock_release_raises_RunTimeError_if_unlocked():
    loop = asyncio.new_event_loop()
    lock = AsyncLock(loop)
    with pytest.raises(RuntimeError):
        loop.run_until_complete(lock.release())


def test_async_lock_acquires_and_releases_in_with_statement():
    loop = asyncio.new_event_loop()
    lock = AsyncLock(loop)

    async def inner():
        assert await lock.locked() is False
        async with lock:
            assert await lock.locked() is True
        assert await lock.locked() is False
    loop.run_until_complete(inner())


def test_async_lock_exposes_inner_lock():
    loop = asyncio.new_event_loop()
    async_lock = AsyncLock(loop)
    thread_lock = async_lock.lock
    thread_lock.acquire()
    assert loop.run_until_complete(async_lock.locked()) is True
    thread_lock.release()
    assert loop.run_until_complete(async_lock.locked()) is False
