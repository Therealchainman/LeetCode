class Solution:
    def majorityElement(self, nums):
        limit=len(nums)/3
        counters=[0,0]
        cands=[None,None]
        # First pass to find the two possible candidates. 
        for elem in nums:
            if elem==cands[0]:
                counters[0]+=1
            elif elem==cands[1]:
                counters[1]+=1
            elif counters[0]==0:
                counters[0]+=1
                cands[0]=elem
            elif counters[1]==0:
                counters[1]+=1
                cands[1]=elem
            elif elem==cands[1]:
                counters[1]+=1
            else:
                counters[0]-=1
                counters[1]-=1
        # Second pass to make sure that both candidates occur more than n/3 times. 
        ans=[]
        for cand in cands:
            if nums.count(cand)>limit:
                ans.append(cand)
        return ans
        