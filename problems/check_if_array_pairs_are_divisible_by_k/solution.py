from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 != 0:
            return False
        d = defaultdict(int)
        count = 0
        for i, a in enumerate(arr):
            key = k - (a % k)
            if d[key] >= 1:
                count += 1
                d[key] -= 1
            else:
                d[a % k or k] += 1
        return len(arr) // 2 == count
		