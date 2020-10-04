class Solution:
    def removeCoveredIntervals(self, A):
        A.sort(key=lambda x: [x[0],-x[1]])
        
        start=A[0][0]
        end=A[0][1]
        n=len(A)
        num_removed=0
        for s,e in A[1:]:
            if s>=start and e<=end:
                num_removed+=1
                continue
            start=s
            end=max(e,end)
        return n-num_removed
            