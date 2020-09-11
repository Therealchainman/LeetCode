class Solution:
    def maxProduct(self, A):
        n=len(A)
        r=A[0]
        imin=imax=r
        for i in range(1,n):
            if A[i]<0:
                imax,imin=imin,imax
            imax=max(A[i],imax*A[i])
            imin=min(A[i],imin*A[i])
            r=max(r,imax)
        return r
            
        