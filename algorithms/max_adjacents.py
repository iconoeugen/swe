#!/usr/bin/python

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        if A is None:
            return 0
        if len(A[0]) == 0:
            return 0
        if len(A[0]) == 1:
            return max(A[0][0], A[1][0])
        
        print("max1")
        max1 = max(A[0][0], A[1][0])
        print("{} {} {}".format(A[0][0], A[1][0], max1))

        for i in range(2, len(A[0]), 2):
            m =  max(A[0][i], A[1][i])
            max1 += m
            print("{} {} {} {}".format(A[0][i], A[1][i], max1, m))

        max2 = max(A[0][1], A[1][1])
        print("max2")
        print("{} {} {}".format(A[0][1], A[1][1], max2))
        for i in range(3, len(A[0]), 2):
            m =  max(A[0][i], A[1][i])
            max2 += m
            print("{} {} {} {}".format(A[0][i], A[1][i], max2, m))
        
        return max(max1, max2)


if __name__ == "__main__":
    sol = Solution()

    A = [[74, 37, 82, 1], [66, 38, 16, 1]]
    A = []
    A.append([16, 5, 54, 55, 36, 82, 61, 77, 66, 61])
    A.append([31, 30, 36, 70, 9, 37, 1, 11, 68, 14])

    print(sol.adjacent(A))