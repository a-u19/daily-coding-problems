"""
Problem #3 [Medium]

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

def serialize(root:Node) -> str:
    if root is None:
        return "None,"
    
    return f"{root.val}," + serialize(root.left) + serialize(root.right)

def deserialize(string:str) -> Node:
    
    def node_to_str(nodes):
        val = nodes.pop(0)
        if val == "None":
            return None
        temp_node = Node(val)
        temp_node.left = node_to_str(nodes)
        temp_node.right = node_to_str(nodes)
        return temp_node

    nodes = string.split(',')
    return node_to_str(nodes[:-1])

if __name__ == '__main__':
    # Construct a tree shown in the above figure
    tree = BinaryTree()
    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("g")
    tree.root.left.left = Node("c")
    tree.root.left.right = Node("d")
    tree.root.left.right.left = Node("e")
    tree.root.left.right.right = Node("f")

'''
Test tree looks like the following:

                a
               / \
              b   g
             / \   
            c   d
               / \ 
              e   f

'''

print(f"Serialized tree is {serialize(tree.root)}")