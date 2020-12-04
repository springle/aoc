from util import timer

from three.a import Forest

PATH = "input"
SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

if __name__ == "__main__":
    with timer():
        solution = 1
        forest = Forest(PATH)
        for slope in SLOPES:
            solution *= forest.count_trees(slope)

        print(solution)
