from math import cos, sin, radians
from typing import List

from twelve.a import Instruction, load_navigator
from util import timer


class Navigator:
    def __init__(self, instructions: List[Instruction]):
        self.instructions = instructions
        self.x, self.y, self.heading = 0, 0, [10, 1]

    def rotate(self, degrees: int):
        r = radians(degrees)
        self.heading = [
            round(cos(r) * self.heading[0] - sin(r) * self.heading[1]),
            round(sin(r) * self.heading[0] + cos(r) * self.heading[1])
        ]

    def move(self, instruction: Instruction):
        print(instruction, self.x, self.y, self.heading)
        if instruction.letter == "L":
            self.rotate(degrees=instruction.number)
        elif instruction.letter == "R":
            self.rotate(degrees=-instruction.number)
        elif instruction.letter == "F":
            self.x += self.heading[0] * instruction.number
            self.y += self.heading[1] * instruction.number
        elif instruction.letter == "N":
            self.heading[1] += instruction.number
        elif instruction.letter == "S":
            self.heading[1] -= instruction.number
        elif instruction.letter == "E":
            self.heading[0] += instruction.number
        elif instruction.letter == "W":
            self.heading[0] -= instruction.number

    def navigate(self):
        for instruction in self.instructions:
            self.move(instruction)


if __name__ == "__main__":
    with timer():
        navigator = load_navigator("input", cls=Navigator)
        navigator.navigate()
        print(abs(navigator.x) + abs(navigator.y))
