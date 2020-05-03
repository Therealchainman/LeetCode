class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        best = 0
        n = len(nums)
        if max(nums) == min(nums):
            return n
        for i in range(1, n + 1):
            greatest = 0
            for j in range(i, n + 1):
                sub = nums[i - 1: j]
                diff = abs(max(sub) - min(sub))
                if diff > limit:
                    break
                else:
                    greatest += 1
            best = max(best, greatest)
        return best