from itertools import product
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R=len(rowSum)
        C=len(colSum)
        M=[[0]*C for _ in range(R)]
        for r,c in product(range(R),range(C)):
            val=min(rowSum[r],colSum[c])
            M[r][c]=val
            rowSum[r]-=val
            colSum[c]-=val
        return M
            