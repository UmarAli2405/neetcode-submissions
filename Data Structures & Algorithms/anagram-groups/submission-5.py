from collections import defaultdict

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = defaultdict(list)
        final_list = []
        for i in range(len(strs)):
            word = strs[i].lower()
            arr = tuple(self.isAnagram(word))

            final_dict[arr].append(word)

        for key, value in final_dict.items():
            final_list.append(value)

        return final_list


    def isAnagram(self, str1 : str):
        arr1 = [0] * 26
        
        for i in str1:
            index = ord(i) - 97
            arr1[index] += 1

        return arr1