import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap_stones = stones

        for i in range(len(stones)):
            heap_stones[i] = -heap_stones[i] #O(n)

        heapq.heapify(heap_stones) #O(logn)

        while len(heap_stones) > 1:

            og_length = len(heap_stones)
            biggest = -heapq.heappop(heap_stones)
            second_biggest = -heapq.heappop(heap_stones)

           

            if biggest != second_biggest:
                heapq.heappush(heap_stones, -biggest - -second_biggest)

            if og_length == 2 and biggest == second_biggest:
                heapq.heappush(heap_stones, -biggest - -second_biggest)

        return -heap_stones[0]