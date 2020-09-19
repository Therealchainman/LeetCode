
import heapq
class Solution:
    def lastStoneWeight(self, stones):
        max_heap=[-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            stone1,stone2=-heapq.heappop(max_heap),-heapq.heappop(max_heap)
            stone_weight=stone1-stone2
            if stone_weight>0:
                heapq.heappush(max_heap,-stone_weight)
        return -max_heap[0] if len(max_heap)==1 else 0