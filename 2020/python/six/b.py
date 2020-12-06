import re
from collections import defaultdict

from util import timer, read_chunks
from six.a import ANSWER_PATTERN


def count_unanimous_answers(path: str) -> list:
    """
    In O(num_lines) time,
    read each groups' answers,
    and count how many are unanimous.
    """
    group_answers = []
    for chunk in read_chunks(path):
        answers, responses = defaultdict(int), list(chunk)
        for response in responses:
            for letter in response:
                if re.match(ANSWER_PATTERN, letter):
                    answers[letter] += 1

        everyone_said_yes = 0
        for answer, count in answers.items():
            if count == len(responses):
                everyone_said_yes += 1

        group_answers.append(everyone_said_yes)

    return group_answers


if __name__ == "__main__":
    with timer():
        print(sum(count_unanimous_answers("input")))
