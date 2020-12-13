from collections import defaultdict

from util import timer, read_number_list

if __name__ == "__main__":
    with timer():
        numbers, sol = sorted(read_number_list("input")), defaultdict(int, {0: 1})
        for num in numbers + [max(numbers) + 3]:
            sol[num] = sol[num - 3] + sol[num - 2] + sol[num - 1]

        print(sol[max(numbers) + 3])
