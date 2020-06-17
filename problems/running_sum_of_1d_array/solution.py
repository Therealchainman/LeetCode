from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
    
"""
[1,2,3,4]
1 + 2
3 + 3
6+ 4
[1,3,6,10]
"""