class Solution:
    def numSubarrayProductLessThanK(self, nums,k):
        
        n=len(nums)
        left=0
        cnt=0
        prod=1
        for right in range(n):
            while left<=right and prod*nums[right]>=k:
                prod//=nums[left]
                left+=1
            cnt=cnt+right-left+1
            prod=1 if left>right else prod*nums[right]
        return cnt