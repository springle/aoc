import functools
import re

from typing import Tuple, List
from dataclasses import dataclass

from util import timer


@dataclass
class Slope:
    x: int
    y: int


class Forest:

    def __init__(self, path: str):
        self.lines = []
        with open(path) as file:
            for line in file:
                self.lines.append(line.strip())

    @functools.lru_cache()
    def get_pattern(self, y: int) -> Tuple[int, List[int]]:
        line = self.lines[y]
        return len(line), [m.start() for m in re.finditer(r"#", line)]

    def is_tree(self, x: int, y: int) -> bool:
        size, indices = self.get_pattern(y)
        return x % size in indices

    def count_trees(self, slope: Slope) -> int:
        return sum([
            self.is_tree(
                x=slope.x * i,
                y=slope.y * i
            ) for i in range(1, len(self.lines) // slope.y)
        ])


if __name__ == "__main__":
    with timer():
        print(Forest("input").count_trees(Slope(x=3, y=1)))
