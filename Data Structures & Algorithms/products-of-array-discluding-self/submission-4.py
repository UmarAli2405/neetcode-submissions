class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * len(nums)
        postfix_arr = [1] * len(nums)

        final_arr = [1]* len(nums)

        b = len(nums) - 2
        for i in range(len(nums) - 1):
            prefix_arr[i+1] = prefix_arr[i] * nums[i]
            postfix_arr[b] = postfix_arr[b+1] * nums[b+1]

            b-=1

        for j in range(len(prefix_arr)):
            final_arr[j] = prefix_arr[j] * postfix_arr[j]

        return final_arr