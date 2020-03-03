#!/bin/python
# Insert sort - stable sorting algorithm (doesn't change the occurrence of two similar elements in the list while sorting)
#
# Time complexity:
#   Big-O:     O(n^2)
#   Big-omega: O(n)
#   Big-theta: O(n^2)
#
# Space complexity:
#   O(1)

def sort(list):
    l = len(list)
    steps = 0

    for i in range(1, l):
        j = i
        while j > 0 and list[j-1] > list[j]:
            list[j-1], list[j] = list[j], list[j-1]
            j -= 1

            steps += 1
            print( "step: {} i: {} j: {} List: {}".format(steps, i, j, list))

    return steps

if __name__ == "__main__":
    list = [4 ,5, 7, 1, 9, 0, 8, 3, 2, 6]

    steps = sort(list)
    print( "step: {} List: {}".format(steps, list))

    assert( list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
