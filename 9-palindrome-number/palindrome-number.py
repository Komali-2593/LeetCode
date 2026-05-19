class Solution:
    def isPalindrome(self,n:int) -> bool:
      

        original = n
        reverse = 0

        while n > 0:
             digit = n % 10
             reverse = reverse * 10 + digit
             n = n // 10

        if original == reverse:
             return True
        else:
            return False
