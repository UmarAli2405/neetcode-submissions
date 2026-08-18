class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        s = s.replace(" ", "")
        index = len(s) - 1
        i = 0

        while i < index:
            while not s[i].isalnum() and i < index:
                i += 1
            while not s[index].isalnum() and index > i:
                index -= 1

            if s[i] != s[index]:
                return False

            i += 1
            index -=1

        
        return True