from util import timer

from four.b import read_passports

if __name__ == "__main__":
    with timer():
        print(len(read_passports("input")))
