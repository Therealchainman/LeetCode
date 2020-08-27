class Solution:
    def twoSum(self, A,target):
        seen={}
        for i,n in enumerate(A):
            if target-n in seen:
                return [seen[target-n]+1,i+1]
            else:
                seen[n]=i
        
        