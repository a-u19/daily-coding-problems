"""
Problem #8 - Google - Count Unival Subtrees- Easy

This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""
import random
###############################################################################################
# solution start
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_unival(node: Node) -> bool:
    if not node.left and not node.right:
        return True
    if not node.left or not node.right:
        return node.val == (node.left.val if node.left else node.right.val)
    return node.val == node.left.val == node.right.val

def count_unival_trees(root:Node) -> int:
    if not root:
        return 0
    left_count = count_unival_trees(root.left)
    right_count = count_unival_trees(root.right)

    if is_unival(root):
        return left_count + right_count + 1
    return left_count + right_count

# solution ends
###############################################################################################

def print_tree(root, prefix="", is_left_child=False):
    if not root:
        return

    connection = "├── " if is_left_child else "└── "
    prefix = prefix + connection

    print(prefix + str(root.val))

    print_tree(root.left, prefix + "│   ", True)
    print_tree(root.right, prefix + "    ", False)

def generate_random_binary_tree(depth=0, max_depth=3):
    if depth > max_depth or random.random() < 0.1:
        return None

    val = random.randint(0, 1)
    left = generate_random_binary_tree(depth + 1, max_depth)
    right = generate_random_binary_tree(depth + 1, max_depth)

    return Node(val, left, right)

if __name__ == '__main__':
    print("Sample test")
    # Create the sample binary tree
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)
    print("The tree looks as below:")
    print_tree(root)
    print(f"and the number of unival trees is {count_unival_trees(root)}")
    print("Random tests")
    rand_tree = generate_random_binary_tree()
    print("The tree looks as below")
    print_tree(rand_tree)
    print(f"and the number of unival trees is {count_unival_trees(rand_tree)}")