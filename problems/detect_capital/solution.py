class Solution:
    def detectCapitalUse(self, w):
        c = 0
        for ch in w:
            if ch.isupper():
                c += 1
        return c == len(w) or (c == 1 and w[0].isupper()) or c == 0
                
        