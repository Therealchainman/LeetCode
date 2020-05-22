import itertools
class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        for key, group in itertools.groupby(s):
            res = max(res, len(list(group)))
        return res

        
"""
Starting this at midnight 12am:
Okay so I get the problem.  I need to return longest substrring.  that contains only one unique character.  
seems quite simple right.  Simple recursion ought to work here. I believe since the following is true. 

"""