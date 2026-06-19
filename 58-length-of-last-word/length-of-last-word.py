class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start=0
        s=s.strip()
        for i in range(len(s)):
            if s[i]==" ":
                start=i+1
        n=s[start:len(s)]
        return len(n)



        
        