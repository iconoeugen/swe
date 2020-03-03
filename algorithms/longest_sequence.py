class Solution:
    class Node():
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def insert(self, node, data):
        if data <= node.data:
            if node.left == None:
                node.left = Solution.Node(data)
            else:
                self.insert(node.left, data)
        else:
            if node.right == None:
                node.right = Solution.Node(data)
            else:
                self.insert(node.right, data)
    
    def inorder(self, node):
        if node == None:
            return

        yield from self.inorder(node.left)

        yield node.data

        yield from self.inorder(node.right)
        
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):

        if len(A) == 0:
            return 0

        root = Solution.Node(A[0])
        
        for i in range(1, len(A)):
            self.insert(root, A[i])

        l = [i for i in self.inorder(root)]

        prev = l[0]
        maximum = 1
        seq = 1
        for i in range(1, len(l)):
            if prev + 1 == l[i]:
                seq += 1
            else:
                seq = 1
            prev = l[i]

            maximum = max(seq, maximum)

        #return self.sequence(root)

        return maximum


if __name__ == "__main__":
    A = [ 100, 4, 200, 1, 3, 2 ]
    sol = Solution()

    print(sol.longestConsecutive(A))