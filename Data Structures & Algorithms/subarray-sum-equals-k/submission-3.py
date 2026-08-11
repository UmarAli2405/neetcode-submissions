class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        dict_sums = {}
        total = 0

        for i in range(len(nums)):
            if prefix_sum in dict_sums:
                dict_sums[prefix_sum] += 1
            else:
                dict_sums[prefix_sum] = 1

            prefix_sum += nums[i]

            if prefix_sum - k in dict_sums:
                total += dict_sums[prefix_sum - k]

        return total