import itertools

from eleven.a import Plane
from util import timer


ADJACENT = [-1, 0, 1]


class BPlane(Plane):
    def look(self, x: int, y: int, xp: int, yp: int):
        if self.width > x + xp >= 0 and self.height > y + yp >= 0:
            return x + xp, y + yp

    def neighbors(self, x: int, y: int) -> int:
        occupied, i = 0, 1
        for xp, yp in itertools.product(ADJACENT, ADJACENT):
            if xp or yp:
                while c := self.look(x, y, xp * i, yp * i):
                    if self.rows[c[1]][c[0]] == ".":
                        i += 1
                    else:
                        occupied += int(self.rows[c[1]][c[0]] == "#")
                        break

                i = 1

        return occupied


if __name__ == "__main__":
    with timer():
        plane = Plane("input")
        while plane.simulate():
            pass

        print(sum(row.count("#") for row in plane.rows))
