from eight.a import load_program, Program, Instruction, InfiniteLoopError
from util import timer, submit


def fix_program(program: Program) -> Program:
    return program


def flip_nop_jmp(instruction: Instruction) -> Instruction:
    if instruction.command == "nop":
        instruction.command = "jmp"
    elif instruction.command == "jmp":
        instruction.command = "nop"

    return instruction


if __name__ == "__main__":
    with timer():
        program = load_program("input")
        for i, instruction in enumerate(program.instructions):
            try:
                if instruction.command != "acc":
                    program.instructions[i] = flip_nop_jmp(instruction)
                    submit(program.run(allow_loops=False))
            except InfiniteLoopError as e:
                program.instructions[i] = flip_nop_jmp(instruction)
                program.reset()

