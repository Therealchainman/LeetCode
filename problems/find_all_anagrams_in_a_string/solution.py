import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        np = len(p)
        ns = len(s)
        cp = collections.Counter(p)
        res = []
        window = Counter()
        for i in range(ns - np + 1):
            if i == 0:
                window = Counter(s[:np])
            else:
                window[s[i-1]] -= 1
                window[s[i + np - 1]] += 1
            if len(window - cp) == 0:
                res.append(i)
        return res