import time

class Timer:
    def __init__(self):
        self.elapsed_time = 0
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time += time.time() - self.start_time
        self.start_time = None

    def reset(self):
        self.elapsed_time = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapper


with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second

time.sleep(1)
with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 seconds

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second

t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds

