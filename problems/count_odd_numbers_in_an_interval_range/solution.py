class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = (high - low) >> 1
        if high % 2 != 0 or low % 2 != 0:
            odd += 1
        return odd
        
    