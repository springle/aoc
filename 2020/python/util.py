import contextlib
import functools
import sys
import time


@contextlib.contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        duration = round(time.time() - start, 8)
        print(f"Completed in {duration} seconds")


@functools.lru_cache()
def input_number_set(path: str = "input") -> set:
    numbers = set()
    with open(path) as file:
        for line in file:
            numbers.add(int(line))

    return numbers


def submit(solution: str):
    print(solution)
    sys.exit(0)
