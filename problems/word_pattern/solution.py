class Solution:
    def wordPattern(self, pattern,sentence):
        A=sentence.split()
        D={}
        B={}
        if len(pattern)!=len(A):
            return False
        for i,p in enumerate(pattern):
            # print(A[i],p)
            if p not in D and A[i] not in B:
                D[p]=A[i]
                B[A[i]]=p
                continue
            if A[i] not in B or p not in D:
                return False
            if D[p]!=A[i] or B[A[i]]!=p:
                return False
        return True
        
        