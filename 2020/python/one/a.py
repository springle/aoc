from util import submit, input_number_set, timer

if __name__ == "__main__":
    with timer():
        for number in input_number_set():
            complement = 2020 - number
            if complement in input_number_set():
                submit(number * complement)
