class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''return sorted(s)==sorted(t)'''
        count=0
        if len(s)!=len(t):
            return False
        t=list(t)
        for ch in s:
            if ch in t:
                t.remove(ch)
                count+=1
        if count==len(s):
            return True
        return False
        