from typing import List

from util import timer, submit


def read_numbers(path: str) -> List[int]:
    numbers = []
    with open(path) as file:
        for line in file:
            numbers.append(int(line.strip()))

    return numbers


TAIL_LEN = 25

if __name__ == "__main__":
    with timer():
        numbers = read_numbers("input")
        for i, num in enumerate(numbers[TAIL_LEN:], TAIL_LEN):
            tail = numbers[i-TAIL_LEN:i]
            for addend in tail:
                if num - addend in tail and num - addend != addend:
                    break
            else:
                submit((i, num))
