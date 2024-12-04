"""
Easy:
This problem was asked by Google,



Given the root of a binary tree return a deepest node. For example, in the following tree, return d.

         a

        /  \

      b     c

    /

d
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_deepest_node(node: Node) -> Node:
    if not node.left and not node.right:
        return node

    left_depth = get_depth(node.left)
    right_depth = get_depth(node.right)

    if left_depth >= right_depth:
        return get_deepest_node(node.left)
    else:
        return get_deepest_node(node.right)


def get_depth(node: Node) -> int:
    if not node:
        return 0
    return 1 + max(get_depth(node.left), get_depth(node.right))

if __name__ == '__main__':
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')

    deepest_node = get_deepest_node(root)
    print(deepest_node.val)  # Output: d

"""
# Problem 19 - Facebook - N Houses K Colours - Medium

This problem was asked by Facebook.
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""
def minCost(costs: list[list[int]]) -> int:
    dp = [0] * len(costs[0])

    for i in range(len(costs)):
        temp_dp = [0] * len(costs[0])
        for j in range(len(costs[i])):
            temp_dp[j] = costs[i][j] + min(dp[:j] + dp[j+1:])
        dp = temp_dp
        print(dp)

    return min(dp)

print(minCost([[50, 60, 70],
               [40, 30, 20],
               [30, 40, 70],
               [50, 30, 60],
               [50, 1, 60]]))