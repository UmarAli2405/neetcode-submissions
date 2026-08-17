class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict = set()

        for i in range(len(nums)):
            if nums[i] in duplicate_dict:
                return True

            duplicate_dict.add(nums[i])

        return False