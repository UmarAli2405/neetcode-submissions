class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 1
        set_nums = set(nums)

        for i in range(len(nums)):
            target = nums[i]
            
            if target - 1 in set_nums:
                continue
                
            current_sequence = 1
            while target + 1 in set_nums:
                current_sequence += 1
                target += 1

                longest_sequence = max(current_sequence, longest_sequence)

        if len(nums) == 0:
            return 0

        return longest_sequence