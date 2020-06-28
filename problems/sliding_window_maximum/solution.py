from collections import deque
class maxQueue(deque):
    
    def enqueue(self, val):
        count = 1
        while self and val > self[-1][0]:
            count += self.pop()[1]
        self.append([val, count])
            
    def dequeue(self):
        self[0][1] -= 1
        if not self[0][1]:
            self.popleft()
    
    def maxVal(self):
        return self[0][0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        maxQ = maxQueue()
        for i in range(len(nums)):
            if i < k - 1:
                maxQ.enqueue(nums[i])
                continue
            maxQ.enqueue(nums[i])
            output.append(maxQ.maxVal())
            maxQ.dequeue()
        return output