#!/bin/python

def sort(list):
    l = len(list)
    steps = 0

    for i in range(0, l-1):
        min_idx = i

        for j in range(i+1, l):
            if list[min_idx] > list[j]:
                min_idx = j

            steps += 1
            print( "step: {} i: {} j: {} min_idx: {} min: {} List: {}".format(steps, i, j, min_idx, list[min_idx], list))

        if list[i] > list[min_idx]:
            list[i], list[min_idx] = list[min_idx], list[i]

    return steps

if __name__ == "__main__":
    list = [4 ,5, 7, 1, 9, 0, 8, 3, 2, 6]

    steps = sort(list)
    print( "step: {} List: {}".format(steps, list))

    assert( list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
