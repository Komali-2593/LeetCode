class Solution:
    def calPoints(self, operations) -> int:
        self.stack=[]
        for record in operations:
            if record.lstrip("-").isdigit():
                self.stack.append(int(record))
            if record=="+":
                self.stack.append(self.stack[-1]+self.stack[-2])
            if record=="D":
                if not self.stack:
                    return False
                self.stack.append(2*self.stack[-1])
            if record=="C":
                self.stack.pop()
        return sum(self.stack)
        