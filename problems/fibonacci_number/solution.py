class Solution:
    def fib(self, N):
        if N==0:
            return 0
        if N==1:
            return 1
        F=[0]*(N+1)
        F[0]=0
        F[1]=1
        for i in range(2,N+1):
            F[i]=F[i-1]+F[i-2]
            # print(F)
        return F[-1]
        