class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
"""
[h,e,l,l,o]
[o,l,l,e,h]
so use a pointer maybe, and have it point to the left or right.          

[h,e,l,r,l,o]
     ^ ^
     O(n)
[o,l,r,l,e,h]
"""
        