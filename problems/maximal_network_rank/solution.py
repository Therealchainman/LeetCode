class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=[set() for _ in range(n)]
        for a,b in roads:
            graph[a].add(b)
            graph[b].add(a)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if j not in graph[i]:
                    ans=max(ans,len(graph[i])+len(graph[j]))
                    continue
                ans=max(ans,len(graph[i])+len(graph[j])-1)
        return ans