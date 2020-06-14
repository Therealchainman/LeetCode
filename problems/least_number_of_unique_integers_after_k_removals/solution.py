from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        s = Counter(arr)
        heap = []
        se = set(arr)
        for a in se:
            heap.append((a, s[a]))
        heap.sort(key=lambda x: x[1], reverse=True)
        for _ in range(k):
            elem, priority = heap[-1]
            priority -= 1
            heap.pop()
            if priority > 0:
                heap.append((elem, priority))
        return len(heap)
        