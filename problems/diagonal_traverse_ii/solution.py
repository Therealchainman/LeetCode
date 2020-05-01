class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        final = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i + j].append(nums[i][j])
        return [v for ls in d.values() for v in ls[::-1]]