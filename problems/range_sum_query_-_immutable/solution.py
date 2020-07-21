class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] + nums
        for i in range(1, len(self.prefix)):
            self.prefix[i] += self.prefix[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix[j + 1] - self.prefix[i]
        
"""
[0,-2,-2,1,-4,-2,-3]

"""

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)