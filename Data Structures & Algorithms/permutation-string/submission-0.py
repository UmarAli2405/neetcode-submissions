from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)

        while right <= len(s2):
            substr = s2[left:right]

            if self.isAnagram(s1, substr):
                print(s1)
                print(substr)
                return True
            
            left += 1
            right +=1 

        return False

    def isAnagram(self, s, s1):
        word_count = defaultdict(int)
        word_count2 = defaultdict(int)

        for i in range(len(s)):
            word_count[s[i]] += 1
            word_count2[s1[i]] += 1
      
        return word_count == word_count2