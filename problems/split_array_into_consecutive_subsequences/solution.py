import heapq as hq
from collections import defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = defaultdict(list)
        for num in nums:
            if num - 1 in d and d[num - 1]:
                hq.heappush(d[num], hq.heappop(d[num - 1]) + 1)
            else:
                hq.heappush(d[num], 1)
        return all(all(n >= 3 for n in d[k]) for k in list(d))


                