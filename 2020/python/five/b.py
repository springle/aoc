from util import timer
from five.a import read_boarding_passes

if __name__ == "__main__":
    with timer():
        boarding_passes = read_boarding_passes("input")
        seat_ids = set(boarding_pass.id for boarding_pass in boarding_passes)
        for boarding_pass in boarding_passes:
            if boarding_pass.id + 2 in seat_ids:
                if boarding_pass.id + 1 not in seat_ids:
                    print(boarding_pass.id + 1)
