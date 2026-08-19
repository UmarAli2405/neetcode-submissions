class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis_map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        paranthesis_stack = []

        for word in s:
            if word in paranthesis_map: #O(1) lookup
                if len(paranthesis_stack) == 0:
                    return False

                top = paranthesis_stack.pop()
                print(top)
                if paranthesis_map[word] != top:
                    return False
            else:
                paranthesis_stack.append(word)

        if len(paranthesis_stack) != 0:
            return False

        return True