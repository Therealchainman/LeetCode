class Solution:
    def combinationSum2(self, cand,target):
        n=len(cand)
        ret=[]
        cand.sort()
        def dfs(target,nums,idx):
            if target==0:
                ret.append(list(nums))
                return
            if target<0:
                return
            for i in range(idx,n):
                
                if i>idx and cand[i]==cand[i-1]:
                    continue
                nums.append(cand[i])
                dfs(target-cand[i],nums,i+1)
                nums.pop()
        dfs(target,[],0)
        return ret