class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = float('inf')
        for x in nums:
            if x == 1:
                if count < k:
                    return False
                count = 0
            else: 
                count += 1
        return True