class DisSet:
    
    def __init__(self, n):
        self.parents = [-1]*n
        self.ranks = [1 for _ in range(n)]
    
    def union(self, u, v):
        if self.ranks[u] > self.ranks[v]:
            self.parents[v] = u
        else:
            self.parents[u] = v
        self.ranks[u] += self.ranks[v]
        self.ranks[v] = self.ranks[u]
        
    def find(self, v):
        start_node = v
        while self.parents[v] != -1:
            v = self.parents[v]
        # path compression
        if start_node != v:
            self.parents[start_node] = v
        return v

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def kruskal():
            dsu = DisSet(n)
            edgess = sorted(edges, key=lambda e: e[2])
            total = 0
            for u, v, w in edgess:
                parent_u = dsu.find(u)
                parent_v = dsu.find(v)
                if parent_u == parent_v:
                    continue
                dsu.union(parent_u, parent_v)
                total += w
            return total
        MST = kruskal()
        critical, pseudo = [], []
        for i in range(len(edges)):
            edges[i][2] += 1
            ST = kruskal()
            if ST > MST:
                critical.append(i)
                edges[i][2] -= 1
            elif ST == MST:  
                edges[i][2] -= 2
                MMST = kruskal()
                if MMST < MST:
                    pseudo.append(i)
                edges[i][2] += 1
        return [critical, pseudo]
                

        
            
        