#!/usr/bin/python

import heapq

def combinations(n, a, b):
    if a is None:
        return []
    if b is None:
        return []

    res = []
    for i in a:
        for j in b:
            heapq.heappush(res, i + j)
            res = heapq.nlargest(n, res)

    return res

if __name__ == '__main__':
    a = [1, 2]
    b = [3, 4]
    n = 2

    combs = combinations(n, a, b)

    print(combs)