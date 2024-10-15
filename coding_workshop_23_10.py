"""
Easy:

This problem was asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


# if nums only contained positive numbers, then all numbers greater than k could be removed but question doesn't specify
def main(target: int, nums: list) -> bool:
    for i, num in enumerate(nums):
        difference = target - num
        if difference in nums[:i] + nums[i + 1:]:
            return True
    return False


def main_three_numbers(target: int, nums: list) -> bool:
    for i, num in enumerate(nums):
        difference = target - num
        if main(target=difference, nums=nums[:i] + nums[i + 1:]):
            return True
    return False


def main_n_numbers(target: int, nums: list, n: int) -> bool:
    if n == 2:
        return main(target, nums)

    for i, num in enumerate(nums):
        difference = target - num
        if main_n_numbers(target=difference, nums=nums[:i] + nums[i + 1:], n=n - 1):
            return True
    return False


testcase1 = [17, [9, 15, 3, 7]]
testcase2 = [20, [10, 3, 5, 7]]
testcase3 = [15, [1, 2, 3, 4, 5]]
print(f"Test case: target = {testcase1[0]}, nums = {testcase1[1]} returns {main(testcase1[0], testcase1[1])}")
print(f"Test case: target = {testcase2[0]}, nums = {testcase2[1]} returns {main(testcase2[0], testcase2[1])}")
print(
    f"Test case: target = {testcase2[0]}, nums = {testcase2[1]} returns {main_three_numbers(testcase2[0], testcase2[1])}")
print(
    f"Test case: target = {testcase3[0]}, nums = {testcase3[1]} returns {main_n_numbers(testcase3[0], testcase3[1], 4)}")


"""
Medium:
 
This problem was asked by Twitter.
 
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have 's' as a prefix. 
 
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
 
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
def autocomplete(query_string:str, string_set:list) -> list:
    autocomplete_dict = {}
    for each_str in string_set:
        for i in range(len(each_str) - 1):
            if each_str[:i+1] in autocomplete_dict.keys():
                autocomplete_dict[each_str[ :i+1]].append(each_str)
            else:
                autocomplete_dict[each_str[ :i+1]] = [each_str]
    # print(autocomplete_dict)
    return autocomplete_dict[query_string]

testcase1 = ["de", ["dog", "deer", "deal"]]
testcase2 = ["app", ["apparently", "apple", "absolute", "appear"]]
print("Sample test:")
print(f"The result to autocomplete {testcase1} is {autocomplete(testcase1[0], testcase1[1])}")
print(f"The result to autocomplete {testcase2} is {autocomplete(testcase2[0], testcase2[1])}")