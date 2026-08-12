class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        my_set = set()

        longest = 0

        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[left])
                left += 1

            sequence = r - left + 1
            longest = max(longest, sequence)
            my_set.add(s[r])

        return longest