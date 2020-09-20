from itertools import product
from functools import lru_cache
class Solution:
    def uniquePaths(self, m,n):
        @lru_cache(None)
        def dp(r,c):
            if r==m-1 and c==n-1:
                return 1
            paths=0
            if r+1<m:
                paths+=dp(r+1,c)
            if c+1<n:
                paths+=dp(r,c+1)
            return paths
        return dp(0,0)
        