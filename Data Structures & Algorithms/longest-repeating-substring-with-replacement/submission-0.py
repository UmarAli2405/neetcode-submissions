from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_count = defaultdict(int)
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            character_count[s[right]] += 1
            target = (right - left + 1) - max(character_count.values())

            while target > k:
                character_count[s[left]] -= 1
                left += 1
                target = (right - left + 1) - max(character_count.values())

            
            max_length = max(max_length, right - left + 1)
            right += 1 

        return max_length