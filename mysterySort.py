# Mystery Sort 1
# What is the time complexity of it?
# What are the limitations of this sort?

def mysterySort1(inputArr):
    arr = [0] * len(inputArr)

    for i in range(0, len(inputArr)):
        arr[(int) (inputArr[i] / 10) - 1] = inputArr[i]

    return arr

def mystery1:
    arr = [45, 29, 12, 76, 67, 88, 100, 34, 52, 92]

    print("Starting Array: ", arr)
    print("Final Array: ", mysterySort(arr))

