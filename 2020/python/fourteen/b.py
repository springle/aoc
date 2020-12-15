import re
from itertools import product

from fourteen.a import MASK_P, MEM_P
from util import timer


def apply_bmask(binary: list, mask: list) -> iter:
    binary = [c if c != "0" else binary[i] for i, c in enumerate(mask)]
    for floating_values in product(["0", "1"], repeat=mask.count("X")):
        xs = iter(floating_values)
        yield int("".join([c if c != "X" else next(xs) for c in binary]), 2)


if __name__ == "__main__":
    with timer():
        with open("input") as file:
            memory = {}
            for line in file:
                try:
                    mask = list(re.match(MASK_P, line.strip()).groups()[0])
                except AttributeError:
                    address, n = re.match(MEM_P, line.strip()).groups()
                    binary = list("{0:b}".format(int(address)).zfill(36))
                    for _address in apply_bmask(binary, mask):
                        memory[_address] = int(n)

            print(sum(memory.values()))
