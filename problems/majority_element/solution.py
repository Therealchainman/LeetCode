class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(nums)
        for x in s:
            if nums.count(x) > n // 2:
                return x
            