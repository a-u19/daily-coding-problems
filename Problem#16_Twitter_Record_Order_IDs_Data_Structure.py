"""
# Problem 16 - Twitter - Record Orders in a Data Structure - Easy

This problem was asked by Twitter.
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
•	record(order_id): adds the order_id to the log
•	get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

# Can use a dictionary and use the order_id as the key
# On second thought, easier to use an array and index items

class Log:
    def __init__(self, max_array):
        self.max_array = max_array
        self.curr_i = 0
        self.arr = []

    def record(self,order_id:int):
        if len(self.arr) == self.max_array:
            self.arr[self.curr_i] = order_id
        else:
            self.arr.append(order_id)
        self.curr_i += 1 % self.max_array

    def get_last(self, i:int):
        return self.arr[self.curr_i - i]