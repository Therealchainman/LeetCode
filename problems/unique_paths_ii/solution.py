from itertools import product
class Solution:
    def uniquePathsWithObstacles(self, A):
        R,C=len(A),len(A[0])
        dp=[[0]*C for _ in range(R)]
        dp[0][0]=1 if A[0][0]==0 else 0
        for r,c in product(range(R),range(C)):
            if r==c==0 or A[r][c]==1:
                continue
            paths=0
            for nr,nc in [(r-1,c),(r,c-1)]:
                if 0<=nr<R and 0<=nc<C and A[nr][nc]==0:
                    paths+=dp[nr][nc]
            dp[r][c]=paths
        return dp[R-1][C-1]