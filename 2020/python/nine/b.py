from util import timer, submit
from nine.a import read_numbers

A_NUM = 507622668

if __name__ == "__main__":
    with timer():
        numbers = read_numbers("input")
        for i, num in enumerate(numbers):
            for j, num2 in enumerate(numbers[i + 1:]):
                num += num2
                if num == A_NUM:
                    block = numbers[i:i+j+2]
                    submit(min(block) + max(block))
                elif num > A_NUM:
                    break
