from collections import defaultdict

from util import timer, read_number_list

if __name__ == "__main__":
    with timer():
        prev, diffs, joltages = 0, defaultdict(int), sorted(read_number_list("input"))
        for number in joltages + [max(joltages) + 3]:
            diffs[number - prev] += 1
            prev = number

        print(diffs[1] * diffs[3])
