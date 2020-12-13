import itertools

from util import timer


class Plane:
    def __init__(self, path: str):
        with open(path) as file:
            self.rows = [line.strip() for line in file]

        self.height = len(self.rows)
        self.width = len(self.rows[0])

    def __str__(self):
        return "\n".join(self.rows)

    def move(self, x: int, y: int, heading: tuple) -> tuple:
        _x, _y = x + heading[0], y + heading[1]
        if self.width > _x >= 0 and self.height > _y >= 0:
            return _x, _y
        else:
            return tuple()

    def neighbors(self, x: int, y: int) -> int:
        occupied = 0
        for heading in itertools.product([-1, 0, 1], [-1, 0, 1]):
            if heading[0] or heading[1]:
                multiplier = 1
                while coordinates := self.move(x, y, (heading[0] * multiplier, heading[1] * multiplier)):
                    char = self.rows[coordinates[1]][coordinates[0]]
                    if char != ".":
                        occupied += int(char == "#")
                        break

                    multiplier += 1

        return occupied

    def transition(self, x: int, y: int) -> str:
        char, neighbors = self.rows[y][x], self.neighbors(x, y)
        if char == "L" and neighbors == 0:
            return "#"
        elif char == "#" and neighbors >= 5:
            return "L"
        else:
            return char

    def simulate(self) -> bool:
        rows = [row[:] for row in self.rows]
        for y, row in enumerate(self.rows):
            rows[y] = "".join([self.transition(x, y) for x, _ in enumerate(row)])

        changed = rows != self.rows
        self.rows = rows
        return changed


if __name__ == "__main__":
    with timer():
        plane = Plane("input")
        while plane.simulate():
            pass

        print(sum(row.count("#") for row in plane.rows))
