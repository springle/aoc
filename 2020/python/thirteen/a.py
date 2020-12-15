from util import timer, submit

if __name__ == "__main__":
    with timer():
        with open("input") as file:
            arrival = int(file.readline().strip())
            ids = [
                int(id) for id in file.readline().strip().split(",")
                if id != "x"
            ]

            i = arrival
            while True:
                for id in ids:
                    if i % id == 0:
                        submit(id * (i - arrival))

                i += 1
