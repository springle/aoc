import re
from typing import List

from util import timer


def search_bsp(bsp: str) -> int:
    low, high = 0, 2 ** len(bsp)
    for letter in bsp:
        half = (high - low) // 2
        if letter in ["F", "L"]:
            high -= half
        else:
            low += half

    return low


class BoardingPass:

    def __init__(self, bsp: str = "FBFBBFFRLR"):
        row_bsp, col_bsp = re.match(r"^([FB]{7})([RL]{3})$", bsp).groups()
        self.row = search_bsp(row_bsp)
        self.col = search_bsp(col_bsp)
        self.id = self.row * 8 + self.col

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


def read_boarding_passes(path: str) -> List[BoardingPass]:
    boarding_passes = []
    with open(path) as file:
        for line in file:
            boarding_passes.append(BoardingPass(bsp=line.strip()))

    return boarding_passes


if __name__ == "__main__":
    with timer():
        boarding_passes = read_boarding_passes("input")
        print(max(boarding_passes).id)
