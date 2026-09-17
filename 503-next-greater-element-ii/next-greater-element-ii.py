class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[-1]*n
        stack=[]
        for i in range(2*len(nums)-1,-1,-1):
            index=i%n
            while stack and stack[-1]<=nums[index]:
                stack.pop()
            if i<n:
                if stack:
                    result[i]=stack[-1]
            stack.append(nums[index])
        return result
        