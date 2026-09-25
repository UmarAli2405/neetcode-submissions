class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            goal = target - nums[i]

            if goal in dict1:
                return [dict1[goal], i]

            dict1[nums[i]] = i

            