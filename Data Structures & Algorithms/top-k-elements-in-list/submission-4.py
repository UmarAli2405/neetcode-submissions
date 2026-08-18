import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        most_frequent = []

        for i in range(len(nums)):
            if nums[i] in freq_dict:
                freq_dict[nums[i]] += 1
            else:
                freq_dict[nums[i]] = 1

       
        for key, val in freq_dict.items():
            heapq.heappush(most_frequent, [val, key])
            if len(most_frequent) > k:
                heapq.heappop(most_frequent)

            
          

   
        final_result = []

        for i in range(len(most_frequent)):
            final_result.append(most_frequent[i][1])

        return final_result