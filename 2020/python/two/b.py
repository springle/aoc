from util import timer

from two.a import parse_records

if __name__ == "__main__":
    with timer():
        num_valid = 0
        for record in parse_records("input"):
            if record.high <= len(record.password):
                low, high = record.password[record.low - 1], record.password[record.high - 1]
                if (low == record.letter) != (high == record.letter):
                    num_valid += 1

        print(num_valid)
