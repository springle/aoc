from util import submit, input_number_set, timer

if __name__ == "__main__":
    with timer():
        for i in input_number_set():
            for j in input_number_set():
                complement = 2020 - i - j
                if complement in input_number_set():
                    submit(i * j * complement)
