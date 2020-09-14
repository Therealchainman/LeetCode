from functools import lru_cache
class Solution:
    def rob(self, nums):
        n=len(nums)
        if n==0:
            return 0
        if n<=2:
            return max(nums)
        dp=[0]*(n)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
            # print(dp)
        return dp[n-1]
        # @lru_cache(None)
        # def dp(i):
        #     if i>=n:
        #         return 0
        #     return max(dp(i+1),nums[i]+dp(i+2))
        # return dp(0)
        