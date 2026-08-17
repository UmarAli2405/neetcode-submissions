from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        duplicate_dict = defaultdict(int)
        duplicate_dict1 = defaultdict(int)
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            
            duplicate_dict[s[i]] += 1
            duplicate_dict1[t[i]] += 1

        if duplicate_dict == duplicate_dict1:
            return True

        return False
