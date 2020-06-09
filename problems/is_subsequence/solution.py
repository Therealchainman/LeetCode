class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        ps, pt = 0, 0
        if ps == ns:
            return True
        while ps < ns and pt < nt:
            if s[ps] == t[pt]:
                ps += 1
                if ps == ns:
                    return True
            pt += 1
        return False
        
        
"""

"""