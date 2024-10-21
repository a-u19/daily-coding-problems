"""
# Problem 14 - Google - Estimate PI - Medium

This problem was asked by Google.
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random

def calculate_pi(num_iterations: int):
    points_in_circle = 0
    for z in range(num_iterations):
        x = random.random()
        y = random.random()

        dist = (x**2 + y**2) ** 0.5

        if dist < 1:
            points_in_circle += 1

    return 4 * points_in_circle / num_iterations

if __name__ == "__main__":
    testcases = [1,10,100,1000,10000,100000,1000000,10000000]
    for testcase in testcases:
        print(f"The number of iterations is {testcase} and pi is {calculate_pi(testcase)}")