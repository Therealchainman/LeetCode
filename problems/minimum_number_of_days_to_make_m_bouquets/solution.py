class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n: 
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            mid = (left + right) >> 1
            num_adj, num_m = 0, 0
            for day in bloomDay:
                if day <= mid:
                    num_adj += 1
                    if num_adj == k:
                        num_m += 1
                        num_adj = 0
                else:
                    num_adj = 0
            # print(num_m)
            # print(mid, left, right)
            if num_m >= m:
                right = mid - 1
            else:
                left = mid + 1
        return left
"""
[1,10,3,10,2]
[1,2,3,4,5,6,7,8,9,10]
left = 1
right = 10
mid = 5
left = 1
right = 4
mid = 2
left = 3
right = 4
3+4=7/2 = 3
mid = 3
left = 3
right = 2
"""

            