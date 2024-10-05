'''
Problem #4 [Hard]


This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''
import random

def main(arr):
    arr.sort()
    prev_num = 0
    for x in arr:
        if x <= 0:
            continue
        elif not prev_num < x < prev_num + 2:
            return prev_num + 1
        prev_num += 1
    return x + 1

if __name__ == '__main__':
    inp1 = [3, 4, -1, 1]
    inp2 = [1, 2, 0]
    print("\nSample tests below:")
    print(f"The input {inp1} gives the result {main(inp1)}")
    print(f"The input {inp2} gives the result {main(inp2)}")
    print("\nRandom tests below:")
    for i in range(5):
        random_inp = [random.randint(-7, 7) for _ in range(7)]
        print(f"The input {random_inp} gives the result {main(random_inp)}")