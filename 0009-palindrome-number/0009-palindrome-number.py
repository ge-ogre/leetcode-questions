class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        elif x < 10:
            return True
        else:
            reverse = 0
            original = x
            while x > 0:
                reverse = (reverse * 10) + (x % 10)
                x = x // 10
            
            return reverse == original