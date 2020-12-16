from util import timer

INPUT = [9, 3, 1, 0, 8, 4]
TURNS = 30000000

if __name__ == "__main__":
    with timer():
        seen, prev = {n: i + 1 for i, n in enumerate(INPUT)}, INPUT[-1]
        for turn in range(len(INPUT), TURNS):
            seen[prev], prev = turn, turn - seen[prev] if prev in seen else 0

        print(TURNS, prev)
