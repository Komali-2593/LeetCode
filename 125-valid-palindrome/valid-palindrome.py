class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for i in range(len(s)):
            if not s[i].isalnum():
                s=s.replace(s[i]," ")
        s=s.replace(" ","")
        
        if s[::1]==s[::-1]:
            return True
        else:
            return False

        