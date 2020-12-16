from collections import defaultdict

from util import timer

if __name__ == "__main__":
    with timer():
        with open("input") as file:
            init = [int(n) for n in file.readline().strip().split(",")]

        turn, seen, prev = 1, defaultdict(list), None
        while turn <= 2020:
            if turn < len(init) + 1:
                n = init[turn - 1]
            else:
                if len(seen[prev]) < 2:
                    n = 0
                else:
                    n = seen[prev][-1] - seen[prev][-2]

            seen[n].append(turn)
            prev = n
            turn += 1

        print(turn, prev)
