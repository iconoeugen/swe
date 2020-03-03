#!/usr/bin/python

class Solution:

    def is_palindrome(self, s):
        l = len(s)
        if l == 1:
            return True
        for i in range(l//2):
            if s[i] != s[l - i - 1]:
                return False
        return True

    def palindrome(self, s, solution, p = []):
        if len(s) == 0:
            solution.append(p[:])

        for pos in range(len(s)):
            if self.is_palindrome(s[0:pos+1]):
                p.append(s[0:pos+1])
                self.palindrome(s[pos+1:], solution, p)
                p.pop()

    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        solution = []
        self.palindrome(A, solution)
        return solution

if __name__ == "__main__":
    solution = Solution()

    solution.is_palindrome("cccaac")

    sol = solution.partition("cccaac")

    print("{}".format(sol))