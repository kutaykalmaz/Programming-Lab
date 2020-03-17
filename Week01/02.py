def SelectionSort(List):
    n = len(List)
    for key in range(n):
        min = key
        for j in range(key+1, n):
            if List[min] > List[j]:
                min = j
        List[key], List[min] = List[min], List[key]
    return List


def Bubble(List):
    n = len(List)
    for i in range(n):
        for j in range(0, n-i-1):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List
