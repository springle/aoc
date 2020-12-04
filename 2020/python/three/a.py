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


PATH = "input"
SLOPE = (3, 1)

if __name__ == "__main__":
    with timer():
        trees, x, y = 0, 0, 0
        forest = Forest(PATH)
        for _ in range(len(forest.lines) // SLOPE[1] - 1):
            x += SLOPE[0]
            y += SLOPE[1]
            if forest.is_tree(x, y):
                trees += 1

        print(trees)
