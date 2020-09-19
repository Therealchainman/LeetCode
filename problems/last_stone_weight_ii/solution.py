class Solution:
    def lastStoneWeightII(self, stones):
        total_weight=sum(stones)
        # Follows similar idea as above where we are going to divide all weights into two groups

        n=len(stones)
        # the dp table contains rows that correspond to stone 0,1,2,3,n-1 stones
        # The column refers to the possible weights from 0,1,2,...,total_weight//2
        dp=[[0]*(total_weight//2+1) for _ in range(n+1)]
        for i in range(1,n+1): # all the items that can be picked
            for j in range(total_weight//2+1):
                if stones[i-1]<=j:  # This case the stone has a weight that is less than current allowed weight
                    dp[i][j] = max(dp[i - 1][j], stones[i - 1] + dp[i - 1][j - stones[i - 1]])
                else: # Cannot pick this stone because weight is greater than weight limit.
                    dp[i][j]=dp[i-1][j] # Thus this stone gets move forward.
        max_weight=dp[n][total_weight//2]
        return total_weight-2*max_weight