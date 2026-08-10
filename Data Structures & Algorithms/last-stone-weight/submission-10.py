import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap_stones = stones
        for i in range(len(heap_stones)):
            heap_stones[i] = -heap_stones[i]

        heapq.heapify(heap_stones)

        while len(heap_stones) > 1:
            biggest = -heapq.heappop(heap_stones)
            second_biggest = -heapq.heappop(heap_stones)

            if biggest > second_biggest:
                heapq.heappush(heap_stones, -(biggest - second_biggest))

        heap_stones.append(0)

        return -heap_stones[0]