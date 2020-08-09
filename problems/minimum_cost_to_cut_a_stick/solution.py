class Solution:
    def minCost(self, n, cuts):
        A=[0]+sorted(cuts)+[n]
        dp=[[0]*len(A) for _ in A]
        
        for i in range(len(A)-2,-1,-1):
            for j in range(i+2,len(A)):
                dp[i][j]=float('inf')
                for k in range(i+1,j):
                    cand=A[j]-A[i]+dp[i][k]+dp[k][j]
                    dp[i][j]=min(dp[i][j],cand)
        return dp[0][-1]
        
        # A=[0]+sorted(cuts)+[n]
        # @lru_cache(None)
        # def dp(i,j):
        #     if i+1>=j:
        #         return 0
        #     ans=float('inf')
        #     for k in range(i+1,j):
        #         ans=min(ans,A[j]-A[i]+dp(i,k)+dp(k,j))
        #     return ans
        # return dp(0,len(A)-1)