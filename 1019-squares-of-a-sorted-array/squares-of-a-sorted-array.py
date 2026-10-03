class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        re=[]
        for i in range(len(nums)):
            num=nums[i] ** 2
            re.append(num)
        re.sort()
        return re
    