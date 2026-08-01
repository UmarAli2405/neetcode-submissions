class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}
        
        for i, n in enumerate(numbers):
            goal = target - n

            if goal in numMap and numMap[goal] != i:
                return [numMap[goal] + 1, i+1]

            numMap[n] = i

            
            

        