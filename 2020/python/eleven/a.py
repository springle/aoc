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

    def neighbors(self, x: int, y: int) -> int:
        indices = [
            (_x, _y)
            for _x, _y in itertools.product([x - 1, x, x + 1], [y - 1, y, y + 1])
            if self.width > _x >= 0 and self.height > _y >= 0 and (_x, _y) != (x, y)
        ]

        return sum(self.rows[_y][_x] == "#" for _x, _y in indices)

    def transition(self, x: int, y: int) -> str:
        char, neighbors = self.rows[y][x], self.neighbors(x, y)
        if char == "L" and neighbors == 0:
            return "#"
        elif char == "#" and neighbors >= 4:
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
