from itertools import combinations
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        cpoints = [complex(x, y) for x, y in points]
        res = 1
        for P, Q in combinations(cpoints, 2):
            M = (P + Q) / 2
            v = M - P
            if abs(v) > r:
                continue
            u = v / abs(v)
            d = (r**2 - abs(v)**2)**0.5
            N = 1j * u
            c1, c2 = M + N * d, M - N * d
            res = max(res, sum(abs(cp - c1) <= r for cp in cpoints))
            res = max(res, sum(abs(cp - c2) <= r for cp in cpoints))
        return res