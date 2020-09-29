class Solution:
    def wordBreak(self, s,A):
        n=len(s)
        dp=[0]*n
        for i in range(n):
            for w in A:

                if s[i-len(w)+1:i+1]==w and (dp[i-len(w)] or i-len(w)+1==0):
                    dp[i]=1
        print(dp)
        return bool(dp[-1])