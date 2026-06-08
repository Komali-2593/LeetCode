class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char in "([{":
                stack.append(char)
            if char==")":
                if not stack or stack[-1]!="(":
                    return False
                stack.pop()
            if char=="}":
                if not stack or stack[-1]!="{":
                    return False
                stack.pop()
            if char=="]":
                if not stack or stack[-1]!="[":
                    return False
                stack.pop()
        if len(stack)==0:
            return True
        else:
            return False
                
            

        
                
            
            