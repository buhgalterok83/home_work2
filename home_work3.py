import functools

def cache_result(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper
@cache_result
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # 5 (вычисление)
print(fibonacci(5))  # 5 (из кэша)
print(fibonacci(10))  # 55 (вычисление)
print(fibonacci(10))  # 55 (из кэша)
