class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=[]
        d=[]
        for i in range(len(senate)):
            if senate[i]=="R":
                r.append(i)
            else:
                d.append(i)
        n=len(senate)
        while r and d:
            R=r.pop(0)
            D=d.pop(0)
            if R<D:
                r.append(R+n)
            else:
                d.append(D+n)
            
        if r:
            return "Radiant"
        if d:
            return "Dire"
            
                

