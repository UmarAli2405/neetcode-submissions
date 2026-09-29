class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = s.upper()
        str1 = str1.replace(" ", "")

        i = 0
        index = len(str1) - 1

        while i < index:
            while str1[i].isalnum() == False and i < index:
                i += 1
            while str1[index].isalnum() == False and index > i:
                index-= 1

            if str1[i] != str1[index]:
                return False

            i+= 1
            index -= 1

        return True
