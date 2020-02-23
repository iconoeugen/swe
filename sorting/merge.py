#!/bin/python
# Merge sort - stable sorting algoritm (doesn't change the occurence of two similar elements in the list while sorting)
#
# Time complexity:
#   Big-O:     O(n * log n)
#   Big-omega: O(n * log n)
#   Big-theta: O(n * log n)
#
# Space complexity:
#   O(n)

def merge(list, low, middle, high):
    first = low
    second = middle+1

    new_list = []

    print("before merge list_low: {} list_end {}, list {}".format(list[low:middle+1], list[middle+1:high+1], list))

    # copy all elements in sorted order until one list is exausted
    while first <= middle and second <= high:
        if list[first] < list[second]:
            new_list.append(list[first])
            first += 1
        else:
            new_list.append(list[second])
            second += 1

    # copy remainig elements from first list
    while first <= middle:
        new_list.append(list[first])
        first += 1

    # copy remaining elements from second list
    while second <= high:
        new_list.append(list[second])
        second += 1

    # overwrite list with new sorted list
    for i in range(low, high+1):
        list[i] = new_list[i - low]

    print("after merge list_low: {} list_end {}, new_list {}".format(list[low:middle+1], list[middle+1:high+1], new_list))

def sort(list, start = None, end = None):
    print("Sort start {} end {}".format(start, end))
    if start == None:
        start = 0
    if end == None:
        end = len(list)-1

    if start >= end:
        return

    middle = (end - start) // 2 + start
    print("Sort start {} end {} middle {}".format(start, end, middle))
    sort(list, start, middle)
    sort(list, middle + 1, end)
    merge(list, start, middle, end)

if __name__ == "__main__":
    list = [4 ,5, 7, 1, 9, 0, 8, 3, 2, 6]

    sort(list)
    print( "Sorted List: {}".format(list))

    assert(list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
