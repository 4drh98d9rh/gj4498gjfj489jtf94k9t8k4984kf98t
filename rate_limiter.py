# rate_limiter.py - Token bucket speed limiter

import asyncio
import time
from app import LINKS

_buckets: dict = {}
_bucket_lock = asyncio.Lock()

MIN_RATE = 1024         # 1 KB/s minimum to avoid zero division
MIN_BURST = 16 * 1024   # 16 KB burst capacity

class _TokenBucket:
    __slots__ = ("rate", "capacity", "tokens", "last_refill")

    def __init__(self, rate_bytes_per_sec: int):
        self.rate = max(rate_bytes_per_sec, MIN_RATE)
        self.capacity = max(self.rate, MIN_BURST)
        self.tokens = self.capacity
        self.last_refill = time.monotonic()

    def _refill(self):
        now = time.monotonic()
        elapsed = now - self.last_refill
        if elapsed > 0:
            self.last_refill = now
            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)

    async def consume(self, n: int):
        while True:
            self._refill()
            if self.tokens >= n:
                self.tokens -= n
                return
            deficit = n - self.tokens
            wait = deficit / self.rate
            await asyncio.sleep(min(max(wait, 0.005), 0.5))

async def throttle(uuid: str, nbytes: int):
    """Apply speed limit if configured. Returns immediately if unlimited."""
    if nbytes <= 0:
        return
    link = LINKS.get(uuid)
    if not link:
        return
    rate = link.get("speed_limit_bytes", 0)
    if rate <= 0:
        return

    # Get or create bucket for this uuid
    async with _bucket_lock:
        bucket = _buckets.get(uuid)
        if bucket is None or bucket.rate != rate:
            bucket = _TokenBucket(rate)
            _buckets[uuid] = bucket

    await bucket.consume(nbytes)

def reset_bucket(uuid: str):
    """Remove bucket when speed limit changes or link is deleted."""
    async def _reset():
        async with _bucket_lock:
            _buckets.pop(uuid, None)
    asyncio.create_task(_reset())