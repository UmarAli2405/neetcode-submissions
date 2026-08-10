import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_values = nums
        heapq.heapify(heap_values)

        while len(heap_values) > k:
            heapq.heappop(heap_values)

        return heap_values[0]
        