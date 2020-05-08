import collections
class monoqueue(collections.deque):
    
    def enqueue(self, val):
        count = 1
        while self and self[-1][0] <= val:
            count += self.pop()[1]
        self.append([val, count])
        
    def dequeue(self):
        ans = self.max()
        self[0][1] -= 1
        if self[0][1] <= 0:
            self.popleft()
        return ans
        
        
    def max(self):
        return self[0][0] if self else 0
        
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        monoq = monoqueue()
        ans = max(nums)
        for index, val in enumerate(nums):
            monoq.enqueue(val + max(0, monoq.max()))
            if index >= k:
                ans = max(ans, monoq.dequeue())
        return max(ans, monoq.dequeue())