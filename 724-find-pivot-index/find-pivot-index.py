class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(0,n):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
        return -1
            
        