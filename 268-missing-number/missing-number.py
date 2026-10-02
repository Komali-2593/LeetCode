class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        if nums[0]!=0:
            return 0
        for i in range(len(nums)):
            a=nums[i]+1
            if a not in nums:
                return a
        
        