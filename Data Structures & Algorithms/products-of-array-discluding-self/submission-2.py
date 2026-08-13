class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = [1] * len(nums)
        right_array = [1] * len(nums)

        index = len(nums) - 2
        for i in range(1, len(nums)):
            left_array[i] = left_array[i-1] * nums[i - 1]
            right_array[index] = right_array[index+1] * nums[index + 1]

            index -= 1
        final_array = [0] * len(nums)
        for i in range(len(final_array)):
            final_array[i] = left_array[i] * right_array[i]


        return final_array