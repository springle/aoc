from util import submit, read_number_set, timer

if __name__ == "__main__":
    with timer():
        for i in read_number_set():
            for j in read_number_set():
                complement = 2020 - i - j
                if complement in read_number_set():
                    submit(i * j * complement)
