"""
# Problem 15 - Facebook - Random Element from Stream of Elements - Medium

This problem was asked by Facebook.
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
# Using random function is probably the easiest method to do this but this would take long to read through the entire stream to find its length

import random
def pick_random(stream):
    random_element = None

    for i, element in enumerate(stream):
        if i == 0:
            random_element = element
        elif random.randint(1, i + 1) == 1:
            random_element = element
    return random_element

# Googled to see other methods