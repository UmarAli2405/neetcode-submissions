import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_values = []

        for i in range(len(nums)):
            heapq.heappush(heap_values, nums[i])
            if len(heap_values) > k:
                heapq.heappop(heap_values)

        return heap_values[0]
        