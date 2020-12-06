import re
from util import timer


def read_group_answers(path: str) -> list:
    group_answers = []
    with open(path) as file:
        for group in file.read().strip().split("\n\n"):
            answers = set()
            for letter in group:
                if re.match(r"[a-z]", letter):
                    answers.add(letter)

            group_answers.append(answers)

    return group_answers


if __name__ == "__main__":
    with timer():
        group_answers = read_group_answers("input")
        print(sum(len(answers) for answers in group_answers))
