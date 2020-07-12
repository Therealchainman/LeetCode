import heapq as hq
from collections import defaultdict
from collections import deque

class Wrap:
    def __init__(self, data):
        self.data = data[1]
        self.edge = data[0]
        
    def __lt__(self, other):
        return self.data > other.data
    
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(deque)
        for i, e in enumerate(edges): 
            u = e[0]
            v = e[1]
            adj[u].append([v, succProb[i]])
            adj[v].append([u, succProb[i]])
        
        heap = []
        for i, x in enumerate(adj[start]):
            obj = Wrap(x)
            hq.heappush(heap, obj)
        while adj[start]:
            adj[start].pop()
        INF = float('inf')
        c = [-INF]*n
        while heap:
            obj = hq.heappop(heap)
            edge, cost = obj.edge, obj.data
            # print(edge, cost)
            if cost > c[edge]:
                c[edge] = cost
            # print(c)
            # print(adj[edge])
            for i, x in enumerate(adj[edge]):
                # print(x)
                x[1] *= cost 
                # print(x)
                obj = Wrap(x)
                hq.heappush(heap, obj)
            while adj[edge]:
                adj[edge].pop()

        return c[end] if c[end] > -INF else 0
    
    
    
    