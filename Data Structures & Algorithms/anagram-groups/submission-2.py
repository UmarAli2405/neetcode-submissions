from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dictionary = defaultdict(list)
        for i in range(len(strs)):
            key_tuple = tuple(self.isAnagram(strs[i]))
            final_dictionary[key_tuple].append(strs[i])
        final_result = []

        for key, value in final_dictionary.items():
            final_result.append(value)
        return final_result
    def isAnagram(self, word):
        self.letter_count = [0] * 26

        new_word = word.upper()

        for i in new_word:
            index = ord(i) - 65
            self.letter_count[index] += 1

        return self.letter_count