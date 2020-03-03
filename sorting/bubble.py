#!/bin/python

# Heap sort - stable sorting algorithm (doesn't change the occurrence of two similar elements in the list while sorting)
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

    for i in range(0, l):
        flag = False
        for j in range(0, l - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                flag = True

            steps += 1
            print( "step: {} i: {} j: {} Flag: {} List: {}".format(steps, i, j, flag, list))

        if not flag:
            break

    print( "steps: {} List: {}".format(steps, list))

if __name__ == "__main__":
    list = [4 ,5, 7, 1, 9, 0, 8, 3, 2, 6]

    sort(list)

    assert( list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
