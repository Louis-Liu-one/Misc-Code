
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    if n == 0:
        return 0
    last, next = 0, 1
    for i in range(1, n):
        last, next = next, last + next
    return next


def fib_iter():
    yield 0
    last, next = 0, 1
    yield next
    while True:
        last, next = next, last + next
        yield next
