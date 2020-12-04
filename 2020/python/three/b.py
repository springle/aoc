from math import prod
from util import timer

from three.a import Forest, Slope

SLOPES = [
    Slope(x=1, y=1),
    Slope(x=3, y=1),
    Slope(x=5, y=1),
    Slope(x=7, y=1),
    Slope(x=1, y=2),
]

if __name__ == "__main__":
    with timer():
        forest = Forest("input")
        print(prod(forest.count_trees(slope) for slope in SLOPES))
