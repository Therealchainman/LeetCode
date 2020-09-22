class Solution:
    def majorityElement(self, nums):
        counter=0
        cand=None
        for integer in nums:
            if counter==0:
                cand=integer
                counter+=1
            elif integer!=cand:
                counter-=1
            else:
                counter+=1
        return cand
            