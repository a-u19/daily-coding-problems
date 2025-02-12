words1, words2 = ["acaac","cccbb","aacbb","caacc","bcbbb"], ["c","cc","b"]
# words1, words2 = ["amazon","apple","facebook","google","leetcode"], ["e","o"]
# words1, words2 = ["amazon","apple","facebook","google","leetcode"], ["lo","eo"]
# words1, words2 = ["amazon","apple","facebook","google","leetcode"], ["ec","oc","ceo"]

res = []

max_letter_dict = {}
for sub_word in words2:
    for char in sub_word:
        try:
            max_letter_dict[char] = max(sub_word.count(char), max_letter_dict[char])
        except KeyError:
            max_letter_dict[char] = sub_word.count(char)

for word in words1:
    exists = True
    word_dict = {letter: word.count(letter) for letter in set(word)}

    for letter_to_compare in max_letter_dict.keys():
        try:
            if word_dict[letter_to_compare] < max_letter_dict[letter_to_compare]:
                exists = False
                break
        except KeyError:
            exists = False
            break

    if exists:
        res.append(word)

print(res)