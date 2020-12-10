import re

from dataclasses import dataclass
from typing import List

from util import timer

INSTRUCTION = re.compile(r"^(\w{3}) ([+-]\d+)$")


@dataclass
class Instruction:
    command: str
    num: int


class InfiniteLoopError(Exception):
    pass


class Program:

    def __init__(self, instructions: List[Instruction]):
        self.instructions = instructions
        self.reset()

    # noinspection PyAttributeOutsideInit
    def reset(self):
        self.acc, self.next_instruction, self.executed_instructions = 0, 0, set()

    def run(self, allow_loops: bool = True) -> int:
        while (
                self.next_instruction not in self.executed_instructions
                and self.next_instruction < len(self.instructions)
        ):
            self.execute(self.instructions[self.next_instruction])

        if not allow_loops:
            if self.next_instruction in self.executed_instructions:
                raise InfiniteLoopError(f"{self.instructions[self.next_instruction]} seen before")

        return self.acc

    def execute(self, instruction: Instruction):
        self.executed_instructions.add(self.next_instruction)
        if instruction.command == "acc":
            self.acc += instruction.num
            self.next_instruction += 1
        elif instruction.command == "jmp":
            self.next_instruction += instruction.num
        elif instruction.command == "nop":
            self.next_instruction += 1


def load_program(path: str) -> Program:
    with open(path) as file:
        instructions = []
        for line in file:
            command, num = re.match(INSTRUCTION, line.strip()).groups()
            instructions.append(Instruction(command, int(num)))

        return Program(instructions)


if __name__ == "__main__":
    with timer():
        print(load_program("input").run())
