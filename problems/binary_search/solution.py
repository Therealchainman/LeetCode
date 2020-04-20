class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, m = 0, len(nums) - 1, 0
        while (1):
            m = int((l + r) / 2)
            if (nums[m] == target):
                return m
            if (m == l and m == r):
                return -1
            if (nums[m] < target):
                l = m + 1
            else:
                r = max(m - 1, 0)