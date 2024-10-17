"""
# Problem 12 - Amazon - N Steps in Staircase - Hard

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that
 returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
•	1, 1, 1, 1
•	2, 1, 1
•	1, 2, 1
•	1, 1, 2
•	2, 2

Part 2:
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers
 X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

Steps - Ways
1 - 1
2 - 2
3 - 3
4 - 5

^ Fib sequence - can be improved using dict to store computed values
"""
import time

def fib_with_no_dict(n:int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return fib_with_no_dict(n - 1) + fib_with_no_dict(n - 2)

def fib_with_dict(n:int) -> int:
    fib_dict = {1:1,
                2:2}

    if n not in fib_dict:
        fib_dict[n] = fib_with_dict(n - 1) + fib_with_dict(n - 2)
    return fib_dict[n]

testcases = [1,2,3,4,5,6,7]
start_time = time.time()
for testcase in testcases:
    print(f"If there are {testcase} number of steps, then there are {fib_with_no_dict(testcase)} number of ways to climb up.")
print(f"Without a dictionary this took {time.time() - start_time}")
start_time = time.time()
for testcase in testcases:
    print(f"If there are {testcase} number of steps, then there are {fib_with_dict(testcase)} number of ways to climb up.")
print(f"With a dictionary this took {time.time() - start_time}")