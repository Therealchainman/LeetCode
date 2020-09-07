class Solution:
    def largestOverlap(self, A,B):
        n=len(A)
        max_count=0
        for dy in range(1-n,n):
            for dx in range(1-n,n):
                count=0
                for x in range(n):
                    for y in range(n):
                        if A[y][x]==1:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<n and 0<=ny<n and B[ny][nx]:
                                count+=1
                max_count=max(max_count,count)
        return max_count
                    