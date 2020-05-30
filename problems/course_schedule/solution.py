class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        # construct graph
        graph = {i: set() for i in range(n)}
        in_degrees = {i:0 for i in range(n)}
        
        for edge in edges:
            graph[edge[0]].add(edge[1])
            in_degrees[edge[1]] += 1
        
        # init var 
        q = collections.deque()
        visited = set()
        
        # find nodes whose in degree == 0
        for index, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(index)
                
        # loop all nodes whose in degree == 0
        while q:
            index = q.popleft()
            visited.add(index)
            for g in graph[index]:
                in_degrees[g] -= 1
                if in_degrees[g] == 0:
                    q.append(g)
        return len(visited) == n
        
        
"""
Start time: 4:36PM
ui
[[0,1],[1,0],[2,3],[1,3]]
so I could take clase
3->1->2
1 -> 0 good

"""