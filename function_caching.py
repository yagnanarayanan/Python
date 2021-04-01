import time
from functools import lru_cache


@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return "Done"


if __name__ == '__main__':
    print(some_work(3))
    print(some_work(4))
    print(some_work(3))
    print(some_work(6))
    print(some_work(6))
