class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_counter = {}

        prefix_sum = 0
        occurrences = 0

        for i in range(len(nums)):

            if prefix_sum in sum_counter:
                sum_counter[prefix_sum] += 1
            else:
                sum_counter[prefix_sum] = 1

            prefix_sum += nums[i] 
            if prefix_sum - k in sum_counter:
                occurrences += sum_counter[prefix_sum - k]

            

            

            
            

        return occurrences