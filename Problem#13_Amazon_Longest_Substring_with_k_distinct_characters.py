"""
# Problem 13 - Amazon - Longest Substring with k distinct characters - Hard

This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
def longest_substring(s:str, k:int) -> tuple:
    head_pointer, tail_pointer = 0, 1
    longest = 0
    while tail_pointer <= len(s):
        if len(set(s[head_pointer : tail_pointer])) == k:
            if (tail_pointer - head_pointer) > longest:
                longest = tail_pointer - head_pointer
        if len(set(s[head_pointer : tail_pointer])) > k:
            head_pointer += 1
        else:
            tail_pointer += 1

    return longest, s[head_pointer:head_pointer + longest]

if __name__ == "__main__":
    testcase1 = ["abcba", 2]
    testcase2 = ["bcbcbcbc", 2]
    testcase3 = ["bcabcbcbc", 2]
    testcase4 = ["abcdaaaa", 1]
    testcase5 = ["abcdeabcde",5]

    testcases = [testcase1, testcase2, testcase3, testcase4, testcase5]

    for testcase in testcases:
        res = longest_substring(testcase[0], testcase[1])
        print(f"The testcase is {testcase} and the longest substring is {res[1]} and the length is {res[0]}")