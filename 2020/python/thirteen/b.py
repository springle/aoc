from util import timer


def load_remainders(path: str) -> list:
    with open(path) as file:
        return [
            (offset, int(n))
            for offset, n in enumerate(file.readlines()[1].strip().split(","))
            if n != "x"
        ]


if __name__ == "__main__":
    with timer():
        time, lcm = 0, 1
        for offset, n in load_remainders("input"):
            while (time + offset) % n != 0:
                time += lcm

            print(time)
            lcm *= n
