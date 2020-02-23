
class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


# Get tree height
def get_tree_height_helper(root, max_height_diff = -1):
    height = 0

    if root == None:
        return -1

    height_left = height
    if root.left != None:
        height_left = get_tree_height_helper(root.left, max_height_diff) + 1

    height_right = height
    if root.right != None:
        height_right = get_tree_height_helper(root.right, max_height_diff) + 1

    if max_height_diff >= 0 and abs(height_left - height_right) > max_height_diff:
        height = -1
    else:
        height = max(height_left, height_right)

    return height

# Check if Perfect binary tree
#  - all interior nodes have two children
#  - all leaves have the same depth or same level
#
#               0
#         1            2
#      11    12   21       22
def is_perfect_binary_tree(root):
    return get_tree_height_helper(root, max_height_diff = 0) > -1

# Check if Balanced binary tree
#  - left and right subtrees' heights differ by at most one
#  - left subtree is balanced
#  - right subtree is balanced
#
#                 0
#          1               2
#      11             21       22
#                                   222
def is_balanced_binary_tree(root):
    return get_tree_height_helper(root, max_height_diff = 1) > -1


# Check if Balanced binary tree
#  - every level, except possibly last, is completely filled
#  - all nodesare as far left as possible
#
#                                0
#               1                              2
#       11             12                 21       22
#  111      112   121      122       221
def is_complete_binary_tree(root):
    raise NotImplementedError()

# Check if Full binary tree
#  - every node has 0 or 2 children
#
#                 0
#          1               2
#                     21            22
#                              221      222
def is_full_binary_tree(root):
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        elif root.left and root.right:
            return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)

        return False

def get_tree_height(root):
    return get_tree_height_helper(root, -1)

def print_tree_inorder(root, depth = 0):
    if root == None:
        return

    print_tree_inorder(root.left, depth +1)
    print('\t'*depth + str(root.data))
    print_tree_inorder(root.right, depth +1)


if __name__ == "__main__":
    full_bt = Node(1)
    full_bt.left = Node(11)
    full_bt.left.left = Node(111)
    full_bt.left.right = Node(112)

    assert(is_balanced_binary_tree(full_bt) == False)

    full_bt.right = Node(12)

    assert(is_full_binary_tree(full_bt))
    assert(get_tree_height(full_bt) == 2)

    assert(is_perfect_binary_tree(full_bt) == False)
    assert(is_balanced_binary_tree(full_bt) == True)

    full_bt.right.left = Node(121)
    assert(is_perfect_binary_tree(full_bt) == False)
    assert(is_balanced_binary_tree(full_bt) == True)


    full_bt.right.right = Node(122)
    assert(is_perfect_binary_tree(full_bt) == True)

    print_tree_inorder(full_bt)
