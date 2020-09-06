class Solution:
    def numTriplets(self, A,B):
        ans=0
        na,nb=len(A),len(B)
        prefix={}
        for i,a in enumerate(A):
            cand=a**2
            if cand in prefix:
                prefix[cand]+=1
                continue
            prefix[cand]=1
        for j,b in enumerate(B):
            for k in range(j+1,nb):
                if b*B[k] in prefix:
                    ans+=prefix[b*B[k]]
        prefix2={}
        
        for i,b in enumerate(B):
            cand=b**2
            if cand in prefix2:
                prefix2[cand]+=1
                continue
            prefix2[cand]=1
        for j,a in enumerate(A):
            for k in range(j+1,na):
                if a*A[k] in prefix2:
                    ans+=prefix2[a*A[k]]
        return ans
        