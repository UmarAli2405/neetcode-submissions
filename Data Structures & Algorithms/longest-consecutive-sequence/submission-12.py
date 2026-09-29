class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        longest = 0
        for num in visited:
            if num - 1 in visited:
                continue

            curr = 1

            while num + 1 in visited:
                curr += 1
                longest = max(curr, longest)
                num = num + 1
            longest = max(curr, longest)

        return longest
        