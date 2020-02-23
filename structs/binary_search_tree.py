#!/bin/python3
# Binary Search Tree
#
# Space            Big Oh(n)          Bit Theta(n)
# Insert           Big Oh(n)          Big Theta(log n)
# Search           Big Oh(n)          Big Theta(log n)
# Traverse         Big Oh(n)          Big Theta(n)

class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def bst_insert(root, data):
    if root == None:
        raise ValueError()
    elif root.data > data:
        if root.left == None:
            root.left = Node(data)
        else:
            bst_insert(root.left, data)
    elif root.data < data:
        if root.right == None:
            root.right = Node(data)
        else:
            bst_insert(root.right, data)

def bst_search(root, data):
    node = None
    if root == None:
        pass
    elif root.data == data:
        node = root
    elif root.data > data:
        node = bst_search(root.left, data)
    elif root.data < data:
        node = bst_search(root.right, data)

    return node

# iterable generator for sorted sequence
def bst_inorder(root):
    if root == None:
        return

    yield from bst_inorder(root.left)
    yield root.data
    yield from bst_inorder(root.right)

def bst_preorder(root):
    if root == None:
        return

    yield root.data
    yield from bst_inorder(root.left)
    yield from bst_inorder(root.right)

def bst_postorder(root):
    if root == None:
        return

    yield from bst_inorder(root.left)
    yield from bst_inorder(root.right)
    yield root.data

def bst_check(root, min = None, max = None):
    if root == None:
        return True

    if min and root.data < min:
        return False
    if max and root.data > max:
        return False

    is_bst = True
    if root.left:
        if root.left.data < root.data:
            is_bst = is_bst and bst_check(root.left, min, root.data)
        else:
            is_bst = False

    if root.right:
        if root.right.data > root.data:
            is_bst = is_bst and bst_check(root.right, root.data, max)
        else:
            is_bst = False

    return is_bst

def print_tree_inorder(root, depth = 0):
    if root == None:
        return

    print_tree_inorder(root.left, depth +1)
    print('\t'*depth + str(root.data))
    print_tree_inorder(root.right, depth +1)

if __name__ == "__main__":
    bst = Node(100)
    bst_insert(bst, 50)
    bst_insert(bst, 75)
    bst_insert(bst, 85)
    bst_insert(bst, 10)
    bst_insert(bst, 30)
    bst_insert(bst, 60)

    bst_insert(bst, 150)
    bst_insert(bst, 175)
    bst_insert(bst, 185)
    bst_insert(bst, 110)
    bst_insert(bst, 130)
    bst_insert(bst, 160)

    assert(bst_check(bst) == True)

    print_tree_inorder(bst)

    assert(bst_search(bst, 150).data == 150)
    assert(bst_search(bst, 99) == None)
    assert(bst_search(bst, 199) == None)
    assert(bst_search(bst, 1) == None)
    assert(bst_search(bst, 101) == None)

    [ print(" {} ".format(d), end='') for d in bst_preorder(bst)]
    print("")
    [ print(" {} ".format(d), end='') for d in bst_inorder(bst)]
    print("")
    [ print(" {} ".format(d), end='') for d in bst_postorder(bst)]
    print("")


    bst_bad = Node(10)
    bst_insert(bst_bad, 5)
    bst_insert(bst_bad, 1)
    bst_insert(bst_bad, 8)
    bst_insert(bst_bad, 7)
    bst_insert(bst_bad, 15)
    bst_bad.left.right.left.right = Node(9)

    print_tree_inorder(bst_bad)

    is_bst = bst_check(bst_bad)
    assert(bst_check(bst_bad) == False)
