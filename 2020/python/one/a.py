from util import submit, read_number_set, timer

if __name__ == "__main__":
    with timer():
        for number in read_number_set():
            complement = 2020 - number
            if complement in read_number_set():
                submit(number * complement)
