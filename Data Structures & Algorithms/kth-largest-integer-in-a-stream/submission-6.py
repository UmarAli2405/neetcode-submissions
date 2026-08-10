import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap_values = nums

        heapq.heapify(self.heap_values)

        while len(self.heap_values) > k:
            heapq.heappop(self.heap_values)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap_values, val)

        if len(self.heap_values) > self.k:
            heapq.heappop(self.heap_values)

        return self.heap_values[0]
