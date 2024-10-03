'''
Problem #2 [Hard]

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''
from functools import reduce

def main_one_liner(arr):
    return [int(reduce(lambda x, y: x * y, arr)/i) for i in arr]

def main(arr):
    total_prod = reduce(lambda x, y: x * y, arr)
    res = [int(total_prod/i) for i in arr]
    return(res)

def follow_up(arr): # can be easily achieved by using a for loop and multiplying during runtime than storing a multiplied value
    res = []
    for i in range(len(arr)):
        total = 1
        for num in (arr[:i] + arr[i+1:]):
            total *= num
        res.append(total)
    return (res)

def follow_up_one_liner(arr):
    return [eval('*'.join(map(str, (arr[:i] + arr[i+1:])))) for i in range(len(arr))]

print(main_one_liner([1, 2, 3, 4, 5]))
print(follow_up_one_liner([5, 6, 7, 8]))