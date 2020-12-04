import functools
import re

from typing import Tuple, List

from util import timer


class Forest:

    def __init__(self, path: str):
        self.lines = []
        with open(path) as file:
            for line in file:
                self.lines.append(line.strip())

    @functools.lru_cache()
    def get_pattern(self, y: int) -> Tuple[int, List[int]]:
        """
        Returns a tuple of the SIZE of the line,
        and the INDICES of trees.
        """
        line = self.lines[y]
        return len(line), [m.start() for m in re.finditer(r"#", line)]

    def is_tree(self, x: int, y: int) -> bool:
        """
        Determine if the coordinate is a tree.

        :param x: 0 = top-left
        :param y: 0 = top-left
        """
        size, indices = self.get_pattern(y)
        return x % size in indices

    def count_trees(self, slope: Tuple[int, int]) -> int:
        trees, x, y = 0, 0, 0
        for index in range(1, len(self.lines) // slope[1]):
            if self.is_tree(
                    x=slope[0] * index,
                    y=slope[1] * index
            ):
                trees += 1

        return trees


PATH = "input"
SLOPE = (3, 1)

if __name__ == "__main__":
    with timer():
        trees = Forest(PATH).count_trees(SLOPE)
        print(trees)
