def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a

    result = 1

    for i in range(b):
        result *= a

    return result


def powerRecursive(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b > 1:
        if b % 2 == 0:
            return powerRecursive(a * a, b / 2)

        return powerRecursive(a * a, b // 2) * a


def findMaxRange(list):
    max = 0

    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            t = 0
            for k in range(i, j + 1):
                t = t + list[k]

            if t > max:
                max = t
                i1, i2 = i, j

    return max, i1, i2


def findMaxRange1(list):  # Less control than the first function.
    max = 0

    for i in range(len(list)):
        t = 0
        for j in range(i, len(list)):
            t = t + list[j]
            if t > max:
                max = t
                i1, i2 = i, j

    return max, i1, i2
