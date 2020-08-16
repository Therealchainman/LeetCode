class Solution:
    def minOperations(self,n):
        ans=0
        A=[]
        for i in range(n):
            A.append(2*i+1)
        for i in range(n-1,-1,-1):
            if A[i] <= n:
                break
            ans+=(A[i]-n)
        return ans
        