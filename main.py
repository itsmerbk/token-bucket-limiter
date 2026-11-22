import time

class TokenBucket:
    def __init__(self, cap, rate):
        self.cap, self.rate, self.tokens, self.last = cap, rate, cap, time.monotonic()
    def allow(self, n=1):
        now = time.monotonic()
        self.tokens = min(self.cap, self.tokens + (now - self.last)*self.rate)
        self.last = now
        if self.tokens >= n: self.tokens -= n; return True
        return False

if __name__ == "__main__":
    tb = TokenBucket(2, 10.0)
    assert tb.allow() and tb.allow() and not tb.allow()
    print("[PASS] 032_token_bucket_limiter")
