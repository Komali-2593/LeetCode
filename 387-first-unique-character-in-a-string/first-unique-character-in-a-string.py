class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            unique=True
            for j in range(len(s)):
                if s[i]==s[j] and i!=j:
                    unique=False
                    break
            if unique:
                return i
        
        return -1

        