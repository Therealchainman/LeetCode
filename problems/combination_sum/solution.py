class Solution:
    def combinationSum(self, A,t):
        self.ans=[]
        n=len(A)
        def dfs(target,cands,idx):
            if target==0:
                self.ans.append(list(cands))
                return
            if target<0:
                return
            
            for i in range(idx,n):
                cands.append(A[i])
                dfs(target-A[i],cands,i)
                cands.pop()
        dfs(t,[],0)
        return self.ans
        