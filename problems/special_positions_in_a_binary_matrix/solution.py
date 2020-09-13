from itertools import product
from collections import defaultdict
class Solution:
    def numSpecial(self, M):
        R,C=len(M),len(M[0])
        ans=0
        def dfs(i,j):
            for r in range(R):
                if M[r][j]==1 and r!=i:
                    return False
            for c in range(C):
                if M[i][c]==1 and c!=j:
                    return False
            return True

        for r,c in product(range(R),range(C)):
            if M[r][c]==1:
                if dfs(r,c):
                    ans+=1
        return ans
            
            
            
        