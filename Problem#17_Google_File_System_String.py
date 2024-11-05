"""
# Problem 17 - Google - File System String - Hard

This problem was asked by Google.
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.is_file = False
        self.longest_path = 0

def longest_absolute_path(input_str):
    stack = []
    max_path_length = 0

    for line in input_str.split('\n'):
        depth = line.count('\t')
        name = line.replace('\t', '')

        while depth < len(stack):
            stack.pop()

        if '.' in name:
            path_length = sum(len(node.val) for node in stack) + len(stack) + len(name)
            max_path_length = max(max_path_length, path_length)
        else:
            stack.append(TreeNode(name))

    return max_path_length


inp1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
inp2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
inputs = [inp1, inp2]

for inp in inputs:
    print(f"The string is \n{inp}\n and the max length of the path is {longest_absolute_path(inp)}")
    print("\n")
