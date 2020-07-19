from collections import deque, defaultdict, Counter
class Solution:
    def countSubTrees(self, n, edges, labels):
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        output = [0 for _ in range(n)]
        def dfs(i, parent):
            counter = Counter()
            for child in tree[i]:
                if child == parent:
                    continue
                counter += dfs(child, i)
            counter[labels[i]] += 1
            output[i] = counter[labels[i]]
            return counter
        dfs(0, None)
        return output
        
"""
approach1:  DFS + backtrack


5
[[0,1],[0,2],[1,3],[0,4]]
"aabab"
6
[[0,1],[0,2],[1,3],[3,4],[4,5]]
"cbabaa"
7
[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]]
"aaabaaa"
4
[[0,2],[0,3],[1,2]]
"aeed"
"""