class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * len(nums)
        postfix_arr = [1] * len(nums)
        index = len(nums) - 2
        for i in range(1, len(nums)):
            prefix_arr[i] = prefix_arr[i-1] * nums[i-1]
            postfix_arr[index] = postfix_arr[index+1] * nums[index+1]

            index -= 1

        final_result = [0] * len(nums)
        for i in range(len(prefix_arr)):
            final_result[i] = prefix_arr[i] * postfix_arr[i]
        
        return final_result