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
        for slope in SLOPES:
            trees, x, y = 0, 0, 0
            forest = Forest(PATH)
            for _ in range(len(forest.lines) // slope[1] - 1):
                x += slope[0]
                y += slope[1]
                if forest.is_tree(x, y):
                    trees += 1

            solution *= trees

        print(solution)
