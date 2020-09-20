class Solution:
    def maxProductPath(self, grid):
        mod=10**9+7
        R,C=len(grid),len(grid[0])
        ans=-1
        dp_pos=[[-1]*C for _ in range(R)]
        dp_neg=[[0]*C for _ in range(R)]
        # dp_neg[0][0]=grid[0][0] 
        stk=[(0,0,grid[0][0])]
        # dp_pos[0][0]=grid[0][0]
        while stk:
            x,y,p=stk.pop()
            if p==0:
                if p>ans:
                    ans=p
                    continue
            if (x,y) == (R-1,C-1):
                if p>ans:
                    ans=p
                continue
            for nx,ny in [(x+1,y),(x,y+1)]:
                if 0<=nx<R and 0<=ny<C:
                    cand=p*grid[nx][ny]
                    if (nx,ny)==(R-1,C-1):
                        cand=p*grid[nx][ny]
                        stk.append((nx,ny,cand))
                    if cand>dp_pos[nx][ny]:
                        dp_pos[nx][ny]=cand
                        stk.append((nx,ny,cand))
                    elif cand<dp_neg[nx][ny]:
                        dp_neg[nx][ny]=cand
                        stk.append((nx,ny,cand))
                                   
        return ans%mod if ans!=-1 else -1