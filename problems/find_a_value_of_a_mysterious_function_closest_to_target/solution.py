class Solution:
    def closestToTarget(self, arr, target):
        s = set()
        mind = float('inf')
        for v in arr:
            ns = set()
            ns.add(v)
            for u in s:
                ns.add(u & v)
            for u in ns:
                mind = min(mind, abs(u - target))
                if mind == 0:
                    return 0
            s = ns
        return mind
    
"""
approach1: using sets lol


"""