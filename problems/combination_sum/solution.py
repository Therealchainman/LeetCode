class Solution:
    def combinationSum(self, cand,target):
        n=len(cand)
        ret=[]
        def dfs(target,nums,idx):
            if target==0:
                ret.append(list(nums))
                return
            if target<0:
                return
            
            for i in range(idx,n):
                nums.append(cand[i])
                dfs(target-cand[i],nums,i)
                nums.pop()
        dfs(target,[],0)
        return ret