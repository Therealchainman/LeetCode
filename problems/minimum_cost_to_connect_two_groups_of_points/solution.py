class Solution:
    def connectTwoGroups(self, cost):
        # kmn graph, so m and n nodes.  Each edge will have a weight or cost and the edges connect from m to n node.
        # It is a bipartite graph. I don't know if I am the best at identifying those issues. 
        M,N=len(cost),len(cost[0])
        mincols=[min(cost[i][j] for i in range(M)) for j in range(N)]
        @lru_cache(None)
        def dp(i,mask):
            # We have matched all left nodes<i
            # and mask nodes on the right
            if i==M:
                ans=0
                for j in range(N):
                    if not mask>>j&1:
                        ans+=mincols[j]
                return ans
            ans=float('inf')
            for j in range(N):
                ans=min(ans,cost[i][j]+dp(i+1,mask|(1<<j)))
            return ans
        return dp(0,0)
        