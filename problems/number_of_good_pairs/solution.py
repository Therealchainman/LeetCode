class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        ans = 0
        for n in nums:
            if n in d:
                ans += d[n]
                d[n] += 1
            else:
                d[n] = 1
        return ans