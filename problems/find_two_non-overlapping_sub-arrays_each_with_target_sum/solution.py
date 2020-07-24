from itertools import accumulate
class Solution:
    def minSumOfLengths(self, arr, target):
        prefixArrayMap = {0: -1}
        INF = float('inf')
        lengths = [INF] * len(arr)
        ans, best = INF, INF
        for i, v in enumerate(accumulate(arr)):
            if v - target in prefixArrayMap:
                l = prefixArrayMap[v - target]
                ans = min(ans, i - l + lengths[l])
                best = min(best, i - l)
            prefixArrayMap[v] = i
            lengths[i] = best
        return ans if ans != INF else -1 
            
        
"""
"""