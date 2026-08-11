import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_values = []

        for i in range(len(points)):
            distance = -self.distance(0, 0, points[i][0], points[i][1])
            heapq.heappush(heap_values, [distance, points[i]])

            if len(heap_values) > k:
                heapq.heappop(heap_values)
        
        final_result = [0] * k

        for i in range(len(heap_values)):
            final_result[i] = heapq.heappop(heap_values)[1]

        return final_result

    def distance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1-y2,2))