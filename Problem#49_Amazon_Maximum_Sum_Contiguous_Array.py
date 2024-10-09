"""
Problem #49 - Amazon - Maximum Sum Contiguous Array - Medium

This problem was asked by Amazon.
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Do this in O(N) time.
________________________________________

"""

'''
Solution:

Keep adding numbers until cuml_sum is below 0 when all numbers preceding and incl num can be removed.
e.g. [34, -50, 42, 14, -5, 86] 
cuml_sum = 34, -16 , ...

Since cuml_sum < 0, it's not beneficial to add 34 and -50 into the final max sum and therefore can be ignored.

Then, cuml_sum = 42, 56, 51, 137

'''
import random

def main(arr):
    cuml_sum = 0
    res_sum = 0
    for num in arr:
        if cuml_sum + num > 0:
            cuml_sum += num
        else:
            cuml_sum = 0
        if res_sum < cuml_sum:
            res_sum = cuml_sum
    print(f"The list is {arr} and the maximum sum of a contiguous subarray is {cuml_sum}.")
        
#
def generate_random_list(num_of_elements):
    rand_list = []
    for i in range(num_of_elements):
        rand_list.append(random.randint(-100,100))
    return rand_list

if __name__ == "__main__":
    main([34, -50, 42, 14, -5, 86])
    main([-5, -1, -8, -9])
    main(generate_random_list(6))