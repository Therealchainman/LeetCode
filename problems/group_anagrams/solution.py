from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mapp = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            mapp[key].append(s)
        for key, val in mapp.items():
            res.append(val)
        return res
          
        
"""
O(n*mlogm)
"""

