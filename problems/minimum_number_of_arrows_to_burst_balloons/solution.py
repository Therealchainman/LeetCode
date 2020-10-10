class Solution:
    def findMinArrowShots(self, A):
        cnt=0
        inf=float('inf')
        minEnd=inf
        A.sort(key=lambda x: [x[0],x[1]])
        for s,e in A:
            if s>minEnd:
                cnt+=1
                minEnd=e
            else:
                minEnd=min(minEnd,e)
        if len(A)==0:
            return cnt
        else:
            return cnt+1
        