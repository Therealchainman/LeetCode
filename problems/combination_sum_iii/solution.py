from itertools import combinations
class Solution:
    def combinationSum3(self, k,n):
        digits=9 if n>=9 else n
        ret=[]
        def dfs(k,n,cand,i):
            if n==0 and k==0:
                ret.append(list(cand))
                return
            if k==0:
                return
            
            if n<=0:
                return
            
            for dig in range(i,digits+1):
                cand.append(dig)
                dfs(k-1,n-dig,cand,dig+1)
                cand.pop()
        dfs(k,n,[],1)
        return ret
        