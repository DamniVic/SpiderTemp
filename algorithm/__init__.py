# user/bin/dev python3
# -*- coding:utf-8 -*-
from random import randint

origin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def compute(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9):
    add = (x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 == 10)
    mul = (
    x0 * 0 + x1 * 1 + x2 * 2 + x3 * 3 + x4 * 4 + x5 * 5 + x6 * 6 + x7 * 7 + x8 * 8 + x9 * 9 == 10)
    return add & mul


if __name__ == '__main__':
    while True:
        x0 = randint(0, 9)
        x1 = randint(0, 9)
        x2 = randint(0, 9)
        x3 = randint(0, 9)
        x4 = randint(0, 9)
        x5 = randint(0, 9)
        x6 = randint(0, 9)
        x7 = randint(0, 9)
        x8 = randint(0, 9)
        x9 = randint(0, 9)
        if compute(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9):
            print(origin)
            print(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)
            break
