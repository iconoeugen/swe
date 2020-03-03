#!/usr/bin/python


class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A <= 2:
            return A
        
        ways = self.climbStairs(A - 1)
        ways+= self.climbStairs(A - 2)
        
        return ways

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.climbStairs(4))