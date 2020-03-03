#!/bin/python
# Heap sort - unstable sorting algorithm (might change the occurrence of two similar elements in the list while sorting)
#
# Time complexity:
#   Big-O:     O(n * log n)
#   Big-omega: O(n * log n)
#   Big-theta: O(n * log n)
#
# Space complexity:
#   O(1)

# make Max-Heap
def heapify(list, depth, root):
    largest = root

    # find children indexes in list as it would be a heap
    left = 2 * root + 1
    right = 2 * root + 2

    # is left child larger than root
    if left < depth and list[left] > list[largest]:
        largest = left

    # is right child larger than root
    if right < depth and list[right] > list[largest]:
        largest = right

    if largest != root:
        list[root], list[largest] = list[largest], list[root]

        # recursively heapify the affected sub-tree
        heapify(list, depth, largest)

def sort(list, l = None):
    if l == None:
        l = len(list)

    # range is exclusive last value
    for i in range( l // 2 - 1, -1, -1):
        heapify(list, l, i)

    for i in range(l-1, 0, -1):
        list[0], list[i] = list[i], list[0]

        heapify(list, i, 0)

if __name__ == "__main__":
    list = [4 ,5, 7, 1, 9, 0, 8, 3, 2, 6]

    sort(list)
    print( "Sorted List: {}".format(list))

    assert(list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
