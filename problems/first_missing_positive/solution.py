class Solution:
    def firstMissingPositive(self, nums):
        n=len(nums)
        nums.append(-1)
        for i in range(n):
            if nums[i]==i+1:
                continue
            x=nums[i]
            while 0<x<=n and x!=nums[x-1]:
                prev=nums[x-1]
                nums[x-1]=x
                x=prev
        
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1