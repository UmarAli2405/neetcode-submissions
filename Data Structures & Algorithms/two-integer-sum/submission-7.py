class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in dict:
                return [dict[goal], i]

            dict[nums[i]] = i

        