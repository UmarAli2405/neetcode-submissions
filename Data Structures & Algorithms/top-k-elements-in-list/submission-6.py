import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        frequent_elements = []
        final_list = []

        for i in range(len(nums)):
            my_dict[nums[i]] += 1 #frequency counter

        for key, value in my_dict.items():    
            heapq.heappush(frequent_elements, (value, key))

            if len(frequent_elements) > k:
                heapq.heappop(frequent_elements)

        for j in range(len(frequent_elements)):
            final_list.append(frequent_elements[j][1])

        return final_list
        