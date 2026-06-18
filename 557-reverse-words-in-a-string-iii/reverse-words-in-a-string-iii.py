class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        start=0
        for i in range(len(s)):
            if s[i]==" ":
                s[start:i]=reversed(s[start:i])
                start=i+1
        s[start:len(s)] = reversed(s[start:len(s)])
                
        return "".join(s)
        