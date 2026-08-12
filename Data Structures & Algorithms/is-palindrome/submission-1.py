class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        new_string = s.replace(" ", "")
        right_index = len(new_string) - 1
        i = 0
        while i < right_index:
           
            while not new_string[i].isalnum() and i < right_index:
                i += 1

            while not new_string[right_index].isalnum() and i < right_index:
                right_index -= 1

            if new_string[i].lower() != new_string[right_index].lower():
                return False

            i += 1
            right_index -= 1

        return True    