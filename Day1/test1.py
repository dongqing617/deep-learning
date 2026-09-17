import numpy as np


def AND(x, y):
    w1 = w2 = 0.5
    b = -0.7
    if (w1 * x + w2 * y + b > 0):
        return 1
    else:
        return 0


def NAND(x, y):
    w1 = w2 = -0.5
    b = 0.7
    if (w1 * x + w2 * y + b > 0):
        return 1
    else:
        return 0


def OR(x, y):
    w1 = w2 = 0.5
    b = -0.3
    if (w1 * x + w2 * y + b > 0):
        return 1
    else:
        return 0


if __name__ == "__main__":
    for i in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y1 = AND(i[0], i[1])
        y2 = NAND(i[0], i[1])
        y3 = OR(i[0], i[1])
        print(y1,y2,y3)
