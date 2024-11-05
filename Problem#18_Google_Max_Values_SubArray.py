"""
# Problem 18 - Google - Max Values of Subarray

This problem was asked by Google.
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
•	10 = max(10, 5, 2)
•	7 = max(5, 2, 7)
•	8 = max(2, 7, 8)
•	8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

"""
import random

def main(arr:list, k:int) -> None:
    if k > len(arr):
        return [max(arr)]
    for i in range(k - 1,len(arr)):
        arr[i + 1 - k] = max(arr[i + 1 - k: i + 1 ])
    return arr[:len(arr) - k + 1]

arr = [10, 5, 2, 7, 8, 7]
k = 3
print(f"The array is {arr} and k is {k} and the resulting array is {main(arr, k)}")

def testing():
    rand_len = random.randint(1,15)
    rand_arr = [random.choice(range(100)) for _ in range(rand_len)]
    k = random.randint(3,10)
    print(f"The array is {rand_arr} and k is {k} and the resulting array is {main(rand_arr, k)}")

for _ in range(5):
    testing()