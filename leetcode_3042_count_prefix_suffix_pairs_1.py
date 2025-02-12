class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        return False if len(str1) > len(str2) else str2[:len(str1)] == str1 and str2[-len(str1):] == str1

    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                print(words[i], words[j])
                if (self.isPrefixAndSuffix(words[i], words[j])):
                    res += 1
                    # print(words[i], words[j])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPrefixAndSuffix('a', 'abb'))