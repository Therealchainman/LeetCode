class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            m = (lo + hi) >> 1
            if nums[m] == target:
                return m
            if nums[m] < target:
                lo = m + 1
            else:
                hi = m - 1
        return lo