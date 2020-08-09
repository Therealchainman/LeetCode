class Solution:
    def findKthBit(self, n,k):
        if n==1:
            return "0"
        S=[0]
        for i in range(1,n):
            T = list(S)
            for i,v in enumerate(T):
                if v == 1:
                    T[i]=0
                else:
                    T[i]=1
            T.reverse()
            S.append(1)
            S.extend(T)
        return str(S[k-1])