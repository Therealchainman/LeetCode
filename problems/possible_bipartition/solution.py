class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        d = {}
        for p in dislikes:
            if p[0] in d:
                d[p[0]].add(p[1])
            else:
                d[p[0]] = set([p[1]])
            if p[1] in d:
                d[p[1]].add(p[0])
            else:
                d[p[1]] = set([p[0]])
        
        seen = {}
        for i in range(N + 1):
            if i not in seen:
                seen[i] = 0
                stack = [i]
                while stack:
                    a = stack.pop()
                    if a in d:
                        for b in d[a]:
                            if b in seen:
                                if seen[b] == seen[a]:
                                    return False
                            else:
                                seen[b] = (seen[a] + 1) % 2
                                stack.append(b)
        return True