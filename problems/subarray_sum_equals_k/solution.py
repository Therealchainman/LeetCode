from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        count = 0
        sumsy = defaultdict(int)
        sumsy[0] = 1
        for val in nums:
            current_sum += val
            count += sumsy[current_sum - k]
            sumsy[current_sum] += 1
        return count
            
            