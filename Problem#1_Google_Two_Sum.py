'''
Problem #1 [Easy]

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
# if nums only contained positive numbers, then all numbers greater than k could be removed but question doesn't specify
def main(target: int, nums: list):
    for num in nums:
        difference = target - num
        if difference in nums:
            return True
    return False

print(main(17, [9, 15, 3, 7]))