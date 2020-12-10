import contextlib
import functools
import sys
import time

from typing import Iterator, TextIO


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


def submit(solution: any):
    print(solution)
    sys.exit(0)


def peek(file: TextIO) -> str:
    pos = file.tell()
    line = file.readline()
    file.seek(pos)
    return line


def read_chunk_of_file(file: TextIO) -> Iterator[str]:
    while line := file.readline():
        if contents := line.strip():
            yield contents
        else:
            break

    while line := peek(file):
        if line.strip():
            break
        else:
            file.readline()
    else:
        file.close()


def read_chunks(path: str) -> Iterator[Iterator[str]]:
    """
    Stream lines of a file grouped together into chunks,
    where each chunk is separated by 1+ empty lines.
    """
    with open(path) as file:
        while not file.closed:
            yield read_chunk_of_file(file)
