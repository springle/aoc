import re

from util import timer

MASK_P = r"^mask = ([X01]+)$"
MEM_P = r"^mem\[(\d+)\] = (\d+)$"


def apply_mask(binary: list, mask: list) -> str:
    for index, char in enumerate(mask):
        if char != "X":
            binary[index] = char

    return "".join(binary)


if __name__ == "__main__":
    with timer():
        with open("input") as file:
            memory = {}
            for line in file:
                try:
                    mask = list(re.match(MASK_P, line.strip()).groups()[0])
                except AttributeError:
                    address, n = [int(x) for x in re.match(MEM_P, line.strip()).groups()]
                    binary = list("{0:b}".format(n).zfill(36))
                    memory[address] = int(apply_mask(binary, mask), 2)

            print(sum(memory.values()))
