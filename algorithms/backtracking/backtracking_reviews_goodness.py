#!/usr/bin/python

class Solution:
    class Goodness():
        def __init__(self, good_words):
            self._good_words_string = good_words
            self._good_words = good_words.split("_")
            
        def get_goodness_level(self, review):
            level = 0
            review_words = review.split("_")
            for w in self._good_words:
                if w in review_words:
                    level += 1
            return level
    
    class ReviewNode():
        def __init__(self, index, review, dictionary):
            self.level = dictionary.get_goodness_level(review)
            self.index = index
            
            self.left = None
            self.right = None
    
    def insert(self, node, root=None):
        if root == None:
            root = node
        elif node.level <= root.level:
            if root.left == None:
                root.left = node
            else:
                self.insert(node, root.left)
        else:
            if root.right == None:
                root.right = node
            else:
                self.insert(node, root.right)
            
        return root
    
    def sort(self, root):
        if root == None:
            return
        
        yield from self.sort(root.right)
        
        yield root.index
        print("{} ".format(root.index))
        
        yield from self.sort(root.left)

    
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        goodness = Solution.Goodness(A)
        
        root = None
        for i in range(len(B)):
            node = Solution.ReviewNode(i, B[i], goodness)
            root = self.insert(node, root)
            
        return [ i for i in self.sort(root)]


if __name__ == "__main__":
    A = "cool_ice_wifi"
    B = [ "water_is_cool", "cold_ice_drink", "cool_wifi_speed" ]

    sol = Solution()
    rev = sol.solve(A, B)

    print(rev)
