class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n=len(A)
        inf=float('inf')
        ans=inf
        for j in range(1,7):
            countA=countB=0
            # This tells me if it is possible to be A or B. 
            isA=isB=True
            for i in range(n):
                if A[i]!=j and B[i]==j:
                    countA+=1
                elif A[i]!=j:
                    isA=False
                if B[i]!=j and A[i]==j:
                    countB+=1
                elif B[i]!=j:
                    isB=False
            if isA:
                ans=min(ans,countA)
            if isB:
                ans=min(ans,countB)
        return ans if ans<inf else -1