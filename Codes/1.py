import random

print(random.random())
rand = random.randint(1, 100)
print(rand)
print("////////////")


def createRandomArray(n, min, max):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min, max))
    return numbers


print(createRandomArray(10, -5, 5))
print("////////////")


def createHist(inlist):
    inHist = dict()
    for i in inlist:
        if i in inHist:
            inHist[i] += 1
        else:
            inHist[i] = 1
    return inHist


list1 = createRandomArray(10, -5, 5)
hist1 = createHist(list1)
print(list1)
print(sorted(list1))
print(list1)
print("////////////")


def createHist_withTuples(inlist):
    freq_list = []
    for i in range(len(inlist)):
        case = False
        for j in range(len(freq_list)):
            if inlist[i] == freq_list[j][0]:
                freq_list[j][1] += 1
                case = True
        if case == False:
            freq_list.append([inlist[i], 1])
    return freq_list


list2 = createRandomArray(10, -5, 5)
tuple1 = createHist_withTuples(list2)
print(list2)
print(sorted(list2))
print(tuple1)
print("////////////")


def findModeValue_withDict(inHist):
    freq_max = -1
    mode = -1
    for key in inHist.keys():
        # print(key, inHist[key])
        if inHist[key] > freq_max:
            freq_max = inHist[key]
            mode = key
    return mode, freq_max


def findModeValue_withTuple(inTuple):
    freq_max = -1
    mode = -1
    for item, freq in inTuple:
        # print(item, freq)
        if freq > freq_max:
            freq_max = freq
            mode = item
    return mode, freq_max


print(findModeValue_withDict(hist1))
print(findModeValue_withTuple(tuple1))
print("////////////")


def LinearSearch(inlist, find):
    search = (-1, -1)
    for index in range(len(inlist)):
        if inlist[index] == find:
            search = (inlist[index], index)
    return search


searchList = createRandomArray(10, -50, 42)
item = LinearSearch(searchList, 5)
print(searchList)
print(item)
print("////////////")


def meanOfList(inlist):
    sum = 0
    count = len(inlist)
    for index in inlist:
        sum += index
        # count += 1
    mean = sum / count
    return mean


meanList = createRandomArray(10, -5, 5)
mean = meanOfList(meanList)
print(meanList)
print(mean)
print("////////////")


def BubbleSorted(inlist):
    n = len(inlist)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if not(inlist[j] < inlist[j+1]):
                inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
    return inlist


bubbleList = createRandomArray(10, -56, 45)
sortedList = BubbleSorted(bubbleList)
print(bubbleList)
print(sortedList)
print("////////////")


def binarySearch(inlist, find):
    search = (-1, -1)
    low, high = 0, len(inlist)-1
    while low <= high:
        mid = (low+high)//2
        if inlist[mid] == find:
            return inlist[mid], mid
        elif inlist[mid] > find:
            high = mid - 1
        else:
            low = mid+1
    return search


searchList = createRandomArray(10, -50, 42)
item = binarySearch(searchList, 9)
print(searchList)
print(item)
print("////////////")


def medianOfList(inlist):
    newInlist = BubbleSorted(inlist)
    n = len(newInlist)
    if n % 2 == 1:
        middle = int(n/2)+1
        median = newInlist[middle - 1]
    else:
        middle_1 = int(n/2) - 1
        middle_2 = middle_1 + 1
        median = (newInlist[middle_1] + newInlist[middle_2]) / 2
    return median


medianList = createRandomArray(10, -50, 42)
median = medianOfList(medianList)
print(medianList)
print(median)
