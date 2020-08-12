from functools import lru_cache
class Solution:
    def minCost(self, n, A):
        A = [0] + sorted(A) + [n]
        dp=[[0]*len(A) for _ in range(len(A))]
        for i in range(len(A)-2,-1,-1):
            for j in range(i+2,len(A)):
                dp[i][j]=float('inf')
                for k in range(i+1,j):
                    dp[i][j]=min(dp[i][j],A[j]-A[i]+dp[i][k]+dp[k][j])
        return dp[0][-1]
        # @lru_cache(None)
        # def dp(i,j):
        #     print(i,j)
        #     print(A[j],A[i])
        #     if i+1>=j:
        #         return 0
        #     ans=float('inf')
        #     for k in range(i+1,j):
        #         ans=min(ans, A[j]-A[i]+dp(i,k)+dp(k,j))
        #     return ans
        # return dp(0,len(A)-1)