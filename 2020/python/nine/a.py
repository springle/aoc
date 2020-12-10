from util import timer, submit, read_number_list

TAIL_LEN = 25

if __name__ == "__main__":
    with timer():
        numbers = read_number_list("input")
        for i, num in enumerate(numbers[TAIL_LEN:], TAIL_LEN):
            tail = numbers[i-TAIL_LEN:i]
            for addend in tail:
                if num - addend in tail and num - addend != addend:
                    break
            else:
                submit((i, num))
