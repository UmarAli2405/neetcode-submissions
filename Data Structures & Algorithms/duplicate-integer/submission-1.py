class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict = {}

        for i in range(len(nums)):
            if nums[i] in duplicate_dict:
                return True
            else:
                duplicate_dict[nums[i]] = 1

        return False