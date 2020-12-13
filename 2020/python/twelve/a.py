import re
from dataclasses import dataclass
from math import cos, sin, radians
from typing import List

from util import timer

INSTRUCTION_PATTERN = re.compile(r"([NSEWLRF])(\d+)")


@dataclass
class Instruction:
    letter: str
    number: int


class Navigator:
    def __init__(self, instructions: List[Instruction]):
        self.instructions = instructions
        self.x, self.y, self.heading = 0, 0, 0

    def move(self, instruction: Instruction):
        if instruction.letter == "L":
            self.heading = (self.heading + instruction.number) % 360
        elif instruction.letter == "R":
            self.heading = (self.heading - instruction.number) % 360
        elif instruction.letter == "F":
            self.x += instruction.number * cos(radians(self.heading))
            self.y += instruction.number * sin(radians(self.heading))
        elif instruction.letter == "N":
            self.y += instruction.number
        elif instruction.letter == "S":
            self.y -= instruction.number
        elif instruction.letter == "E":
            self.x += instruction.number
        elif instruction.letter == "W":
            self.x -= instruction.number

    def navigate(self):
        for instruction in self.instructions:
            self.move(instruction)


def load_navigator(path: str, cls: any = Navigator) -> Navigator:
    instructions = []
    with open(path) as file:
        for line in file:
            letter, number = re.match(INSTRUCTION_PATTERN, line.strip()).groups()
            instructions.append(Instruction(letter=letter, number=int(number)))

    return cls(instructions=instructions)


if __name__ == "__main__":
    with timer():
        navigator = load_navigator("input")
        navigator.navigate()
        print(abs(navigator.x) + abs(navigator.y))
