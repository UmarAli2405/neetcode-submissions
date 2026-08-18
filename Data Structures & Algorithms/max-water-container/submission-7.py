class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[4, 1, 3, 9, 8, 3] (len: 6)
        # l     r      
        #max_area = 16
        max_area = 0
        left = 0
        right = len(heights) - 1 

        while left < right:
            width = right - left 
            height = min(heights[left], heights[right]) 

            area = width * height
            max_area = max(max_area, area) 

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

        # max_area = 0
        # for i in range(len(heights)):
        #     curr = heights[i]
        #     for j in range(i + 1, len(heights)):
        #         width = j - i
        #         height = min(curr, heights[j])

        #         area = width * height
        #         max_area = max(max_area, area)

        # return max_area