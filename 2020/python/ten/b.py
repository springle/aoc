import functools
from typing import Tuple

from util import timer, read_number_list


@functools.lru_cache()
def num_arrangements(numbers: Tuple[int]) -> int:
    if len(numbers) <= 2:
        return 1
    else:
        total = 0
        for index, number in enumerate(numbers[::-1][1:]):
            if numbers[-1] - number <= 3:
                total += num_arrangements(numbers[: -1 - index])

        return total


if __name__ == "__main__":
    with timer():
        numbers = sorted(read_number_list("input"))
        print(num_arrangements(tuple([0] + numbers + [max(numbers) + 3])))
