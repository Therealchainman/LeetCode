from collections import deque
class Solution:
    def orangesRotting(self, G):
        R,C=len(G),len(G[0])
        dq = deque()
        noFresh = True
        mins=0
        # Iterate through the grid to add any 2s to the deque as starting places. 
        for r in range(R):
            for c in range(C):
                if G[r][c] == 2:
                    dq.append((r,c,0))
                elif G[r][c] == 1:
                    noFresh=False
        # return if there is no 1s in the grid.
        if noFresh:
            return mins
        vis=set()
        # BFS to change the 2 to 1 for every 4 directional cell. 
        while dq:
            r, c, m = dq.popleft()
            if (r,c) in vis:
                continue
            vis.add((r,c))
            for rr, cc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0<=rr<R and 0<=cc<C and G[rr][cc] == 1 and (rr,cc) not in vis:
                    G[rr][cc]=2
                    dq.append((rr,cc,m+1))
        # Iterating through to check if there still exist a 1 if so return -1
        for r in range(R):
            for c in range(C):
                if G[r][c] == 1:
                    return -1
        return m
        
        