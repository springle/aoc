import re

from util import timer, read_chunks

ANSWER_PATTERN = re.compile(r"[a-z]")


def read_group_answers(path: str) -> list:
    group_answers = []
    for chunk in read_chunks(path):
        answers = set()
        for line in chunk:
            for letter in line:
                if re.match(ANSWER_PATTERN, letter):
                    answers.add(letter)

        group_answers.append(answers)

    return group_answers


if __name__ == "__main__":
    with timer():
        print(sum(len(answers) for answers in read_group_answers("input")))
