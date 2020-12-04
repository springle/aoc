import re

from dataclasses import dataclass
from typing import List


@dataclass
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str = None

    def is_valid(self):
        try:
            assert 4 == len(self.byr) == len(self.iyr) == len(self.eyr)
            assert 1920 <= int(self.byr) <= 2002
            assert 2010 <= int(self.iyr) <= 2020
            assert 2020 <= int(self.eyr) <= 2030
            assert re.match(r"^#[0-9a-f]{6}$", self.hcl)
            assert self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            assert re.match(r"^\d{9}$", self.pid)
            height, unit = re.match(r"^(\d+)(in|cm)$", self.hgt).groups()
            if unit == "cm":
                assert 150 <= int(height) <= 193
            elif unit == "in":
                assert 59 <= int(height) <= 76

            return True
        except (AssertionError, AttributeError):
            return False


def read_passports(path: str) -> List[Passport]:
    passports = []
    with open(path) as file:
        for record in file.read().split("\n\n"):
            fields = [field.split(":") for field in re.split(r"[ \n]", record.strip())]
            try:
                passports.append(
                    Passport(**{field[0]: field[1] for field in fields})
                )
            except TypeError:
                pass

    return passports


if __name__ == "__main__":
    print(len([p for p in read_passports("input") if p.is_valid()]))
