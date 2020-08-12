class Solution:
    def hIndex(self, A):
        n=len(A)
        counter = [0]*(n+1)
        for a in A:
            if a > n:
                counter[n]+=1
            else:
                counter[a]+=1
        tot=0
        for i in range(n,-1,-1):
            tot += counter[i]
            if tot>=i:
                return i
        return 0
        
        