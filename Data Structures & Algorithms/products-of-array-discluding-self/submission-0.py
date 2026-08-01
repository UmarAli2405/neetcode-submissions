class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]  * len(nums)

        for curr in range(len(output)):
            for i, n in enumerate(nums):
                if i != curr:
                    output[curr] *= n

        return output
        