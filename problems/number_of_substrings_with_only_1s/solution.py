class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        s = list(s)
        def dfs(i):
            count = 0
            for j in range(i, len(s)):
                if s[j] == "1":
                    count += 1
                    s[j] = "0"
                else:
                    break
            return count
        l = []
        n = 0
        for i, c in enumerate(s):
            if c == "1":
                count = dfs(i)
                if count > n:
                    n = count
                l.append(count)
        dp = [0]*(n + 1)
        for i in range(1, n + 1):
            dp[i] += dp[i - 1] + i
        ans = 0
        for x in l:
            ans += dp[x]
        return ans % MOD
            
                
        
        
"""
0110111
 ^
1 - 1
2 - 3
3 - 6
4 - 10
5 - 15
6 - 21
"""