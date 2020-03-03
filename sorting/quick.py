#!/bin/python
# Quick sort - unstable sorting algorithm (might change the occurrence of two similar elements in the list while sorting)
#
# Time complexity:
#   Big-O:     O(n^2)
#   Big-omega: O(n * log n)
#   Big-theta: O(n * log n)
#
# Space complexity:
#   O(n * log n)

def partition(list, start, end):
    # index for elements smaller then pivot
    low = start

    # iterate all elements except last one that is used as pivot
    for i in range(start, end):
        if list[i] < list[end]:
            list[low], list[i] = list[i], list[low]
            low += 1

    # copy pivot in the right position
    list[low], list[end] = list[end], list[low]

    return low

def sort(list, start = None, end = None):
    if not start:
        start = 0
    if not end:
        end = len(list)-1

    if start >= end:
        return

    pivot = partition(list, start, end)
    sort(list, start, pivot-1)
    sort(list, pivot + 1, end)

if __name__ == "__main__":
    list = [4 ,5, 7, 1, 9, 0, 8, 3, 2, 6]

    sort(list)
    print( "Sorted List: {}".format(list))

    assert(list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
