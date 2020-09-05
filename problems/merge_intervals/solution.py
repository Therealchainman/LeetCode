class Solution:
    def merge(self, A):
        n=len(A)
        if n<=1:
            return A
        A.sort()
        ret=[A[0]]
        for i in range(1,n):
            s,e=A[i]
            if ret[-1][1]>=s:
                ret[-1][1]=max(ret[-1][1],e)
            else:
                ret.append(A[i])
        return ret
        