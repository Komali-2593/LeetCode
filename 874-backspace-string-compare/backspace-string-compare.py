class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        self.stack1=[]
        self.stack2=[]
        for char in s:
            if char=="#":
                if not self.stack1:
                    self.stack1.append(char)
                    
                self.stack1.pop()
            else:
                self.stack1.append(char)
        for char in t:
            if char=="#":
                if not self.stack2:
                    self.stack2.append(char)
                self.stack2.pop()
            else:
                self.stack2.append(char)
        return self.stack1==self.stack2
        