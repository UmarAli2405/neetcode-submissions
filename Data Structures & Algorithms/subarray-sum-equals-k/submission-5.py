class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {}
        total = 0

        prefix_arr = [0] * len(nums)
        prefix_arr[0] = nums[0]

        if prefix_arr[0] == k:
            total += 1

        sum_map[0] = 1
        
        if prefix_arr[0] in sum_map:
            sum_map[prefix_arr[0]] += 1
        else:
            sum_map[prefix_arr[0]] = 1

        for i in range(1, len(nums)):

            prefix_arr[i] = prefix_arr[i-1] + nums[i]
            goal = prefix_arr[i] - k

            if goal in sum_map:
                total += sum_map[goal]

            if prefix_arr[i] in sum_map:
                sum_map[prefix_arr[i]] += 1
            else:
                sum_map[prefix_arr[i]] = 1
            
        print(prefix_arr)
            

        return total