class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final_result = [0] * len(temperatures)
        min_stack = []

        for i, t in enumerate(temperatures):
            while len(min_stack) != 0 and t > min_stack[-1][0]:
                top = min_stack.pop()
                final_result[top[1]] = i - top[1]
            else:
                min_stack.append((t, i))
                    
        return final_result
            