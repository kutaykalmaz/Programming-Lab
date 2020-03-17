def InsertionSort(List):
    n = len(List)
    for i in range(1, n):
        key = List[i]
        j = i - 1
        while j >= 0 and key < List[j]:
            List[j+1] = List[j]
            j = j - 1
        List[j+1] = key
    return List


def ShellSort(List):
    n = len(List)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = List[i]
            j = i
            while j >= gap and List[j-gap] > temp:
                List[j] = List[j-gap]
                j = j - gap
            List[j] = temp
        gap //= 2
    return List
