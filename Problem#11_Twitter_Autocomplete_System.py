"""
# Problem 11 - Twitter - Autocmplete System - Medium

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have 's' as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


def autocomplete(query_string: str, string_set: list) -> list:
    autocomplete_dict = {}
    for each_str in string_set:
        for i in range(len(each_str) - 1):
            if each_str[:i + 1] in autocomplete_dict.keys():
                autocomplete_dict[each_str[:i + 1]].append(each_str)
            else:
                autocomplete_dict[each_str[:i + 1]] = [each_str]
    # print(autocomplete_dict)
    return autocomplete_dict[query_string]


testcase1 = ["de", ["dog", "deer", "deal"]]
testcase2 = ["app", ["apparently", "apple", "absolute", "appear"]]
print("Sample test:")
print(f"The result to autocomplete {testcase1} is {autocomplete(testcase1[0], testcase1[1])}")
print(f"The result to autocomplete {testcase2} is {autocomplete(testcase2[0], testcase2[1])}")