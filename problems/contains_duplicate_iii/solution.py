class Solution:
    def containsNearbyAlmostDuplicate(self, nums,k,t):
        buckets={}
        for i,v in enumerate(nums):
            bn,offset=(v//t,1) if t else (v,0)
            for j in range(bn-offset,bn+offset+1):
                if j in buckets and abs(buckets[j]-v)<=t:
                    return True
            buckets[bn]=v
            if len(buckets)>k:
                del buckets[nums[i-k]//t if t else nums[i-k]]
        return False
        