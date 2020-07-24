class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for v in nums:
            if v not in s:
                s.add(v)
            else:
                s.remove(v)
        return list(s)