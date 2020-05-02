class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = list()
        g = max(candies)
        return [True if c + extraCandies >= g else False for c in candies]
            