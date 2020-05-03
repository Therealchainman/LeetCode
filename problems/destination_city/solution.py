class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict()
        s = set()
        for t in paths:
            d[t[0]] = t[1];
        for x in paths:
            s.add(x[0])
            s.add(x[1])
        for x in s:
            if x not in list(d):
                return x