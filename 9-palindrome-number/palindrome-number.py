class Solution:
    def isPalindrome(self,n:int) -> bool:
        if n<0:
            return False
        rev = int(str(n)[::-1])
        
        return n==rev
