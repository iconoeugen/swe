
import math

def binary_search(arr, x, low = None, high = None):
    """Jump search

    Arguments:
        arr: array containing the values
        x: value to look for

    Returns:
        int: index in array where value x is found, otherwise -1
    """
    if low == None:
        low = 0
    if high == None:
        high = len(arr) - 1

    if low > high:
        return -1

    middle = low + (high - low) // 2

    if arr[middle] > x:
        return binary_search(arr, x, low, middle -1)
    elif arr[middle] < x:
        return binary_search(arr, x, middle + 1, high)

    return middle

def jump_search(arr, x):
    """Jump search

    Arguments:
        arr: array containing the values
        x: value to look for

    Returns:
        int: index in array where value x is found, otherwise -1
    """
    n = len(arr)
    step = int(math.sqrt(n))
    start = 0

    while start + step < n and x > arr[start + step]:
        start += step

    for i in range(start, min(start + step + 1, n)):
        if arr[i] == x:
            return i

    return -1

if __name__ == "__main__":
    # Driver code to test function
    arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 ]

    x = 30
    assert(binary_search(arr, x) == -1)
    assert(jump_search(arr, x) == -1)

    x = -1
    assert(binary_search(arr, x) == -1)
    assert(jump_search(arr, x) == -1)

    x = 0
    assert(binary_search(arr, x) == 0)
    assert(jump_search(arr, x) == 0)

    x = 55
    index = binary_search(arr, x)
    assert(binary_search(arr, x) == 10)
    assert(jump_search(arr, x) == 10)

    x = 610
    assert(binary_search(arr, x) == -1)
    assert(jump_search(arr, x) == -1)

    arr.append(610)

    x = 610
    assert(binary_search(arr, x) == 15)
    assert(jump_search(arr, x) == 15)

    arr.append(888)

    x = 610
    assert(binary_search(arr, x) == 15)
    assert(jump_search(arr, x) == 15)

    x = 888
    assert(binary_search(arr, x) == 16)
    assert(jump_search(arr, x) == 16)
