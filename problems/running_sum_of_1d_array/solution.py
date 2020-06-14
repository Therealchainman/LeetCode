from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = accumulate(nums)
        return list(res)