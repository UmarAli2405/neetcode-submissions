class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}

        for i in range(len(nums)):
            goal = target - nums[i]

            if goal in target_map :
                return [target_map[goal], i]

            target_map[nums[i]] = i
        

            

        return []