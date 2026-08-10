from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS = defaultdict(int)
        dictT = defaultdict(int)

        for i in range(len(s)):
            dictS[s[i]] += 1
            dictT[t[i]] += 1

        for key, val in dictS.items():
            if dictS[key] != dictT[key]:
                return False

        
        return True