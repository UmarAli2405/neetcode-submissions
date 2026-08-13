class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        my_set = set()

        right = 0
        longest_sequence = 0

        while right < len(s):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            
            my_set.add(s[right])

            longest_sequence = max(longest_sequence, len(my_set))
            right += 1
        return longest_sequence