class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=[]
        count=0
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                num.append(nums[i])
                count+=1
                
        num.append(nums[-1])
        for i in range(len(num)):
            nums[i] = num[i]

        return len(num)


      