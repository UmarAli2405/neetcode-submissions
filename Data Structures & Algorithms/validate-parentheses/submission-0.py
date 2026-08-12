class Solution:
    def isValid(self, s: str) -> bool:
        character_keys = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        my_stack = []

        for word in s:
            if word in character_keys:
                if len(my_stack) == 0:
                    return False
                top = my_stack.pop()
                if top != character_keys[word]:
                    return False
            else:
                my_stack.append(word)

        if len(my_stack) != 0:
            return False
        
        return True