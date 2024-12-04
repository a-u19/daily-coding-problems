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