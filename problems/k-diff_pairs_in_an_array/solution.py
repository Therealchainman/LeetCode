from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n=len(nums)
        
        counts=Counter(nums)
        num_pairs=0
        if k>0:
            for integer in counts:
                if integer+k in counts:
                    num_pairs+=1
        else:
            for cnt in counts.values():
                if cnt>1:
                    num_pairs+=1
        return num_pairs