from dataclasses import dataclass
from typing import List

from util import timer


@dataclass
class Record:
    password: str
    letter: str
    low: int
    high: int


def parse_records(path: str) -> List[Record]:
    with open(path) as file:
        records = []
        for line in file:
            policy, password = line.split(":")
            frequency, letter = policy.split(" ")
            low, high = [int(num) for num in frequency.split("-")]
            records.append(
                Record(
                    password=password.strip(),
                    letter=letter,
                    low=low,
                    high=high
                )
            )

    return records


if __name__ == "__main__":
    with timer():
        num_valid = 0
        for record in parse_records("input"):
            if record.low <= record.password.count(record.letter) <= record.high:
                num_valid += 1

        print(num_valid)
