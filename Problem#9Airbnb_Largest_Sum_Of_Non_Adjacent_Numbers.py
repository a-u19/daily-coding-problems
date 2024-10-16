"""
#Problem 9 - Airbnb - Largest sum of non-adjacent numbers

This problem was asked by Airbnb.
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
"""

import random

# compare pairs of adjacent numbers and if two selected nums are adjacent, then find the larger set
def solve(nums_list: list) -> int:
    last_num = 0
    penultimate_num = 0

    for i in range(len(nums_list)):
        new_last = max(nums_list[i], nums_list[i] + penultimate_num, last_num)

        penultimate_num = last_num
        last_num = new_last

    return last_num

testcase1 = [2, 4, 6, 2, 5]
print(f"Sample test below:\nThe solution to {testcase1} is {solve(testcase1)}")
print("\nRandom tests below:")
for i in range(5):
    random_inp = [random.randint(-7, 20) for _ in range(7)]
    print(f"The input {random_inp} gives the result {solve(random_inp)}")