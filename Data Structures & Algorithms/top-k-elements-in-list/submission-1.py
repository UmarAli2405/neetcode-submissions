from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap_values = []

        for num, freq in count.items():
          heapq.heappush(heap_values, (freq, num))

          if len(heap_values) > k:
            heapq.heappop(heap_values)

        final_result = [0] * k

        for i in range(k):
          final_result[i] = heapq.heappop(heap_values)[1]

        return final_result